# Day 49 - Automate Gym Bookings
# Automating gym bookings

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time

ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]
GYM_URL = os.environ["GYM_URL"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying  {description}. Attempt: {i+1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, value="password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, value="submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked")

retry(login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
class_booked = 0
class_waitlist = 0
class_already = 0
processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            class_info = f"{class_name} on {day_title}"
            if "Book Class" == button.text:
                button.click()
                class_booked += 1
                print(f"Booked: {class_name} on {day_title}")
                processed_classes.append(f"[Successfully booked:] {class_info}")
            elif "Booked" == button.text:
                class_already += 1
                print(f"Already booked: {class_name} on {day_title}")
                processed_classes.append(f"[Booked] {class_info}")
            elif "Join Waitlist" == button.text:
                button.click()
                class_already += 1
                print(f"Joined waitlist for: {class_name} on {day_title}")
                processed_classes.append(f"[New Waitlist] {class_info}")
            elif "Waitlisted" == button.text:
                class_waitlist += 1
                print(f"Already on waitlist: {class_name} on {day_title}")
                processed_classes.append(f"[Waitlisted] {class_info}")

total_booked = class_booked + class_waitlist + class_already
print(f"Total Tuesday and Thursday 6pm classes processed: {total_booked}")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

def get_my_bookings():
    my_bookings = wait.until(ec.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings.click()

    wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
    book_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-']")
    if not book_cards:
            raise TimeoutException("No booking cards found - page may not have loaded")
    return book_cards

all_cards = retry(get_my_bookings, description="Get my bookings")
verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

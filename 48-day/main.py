# Day 48 - Cookie Clicker Bot
# Automating cookie clicker to do better things with my time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

sleep(2)

cookie = driver.find_element(By.ID, value="bigCookie")

wait_time = 10
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            product = driver.find_elements(By.CSS_SELECTOR, value="div[id^='product")

            for product in reversed(product):
                if "enabled" in product.get_attribute("class"):
                    product.click()
        except (NoSuchElementException, ValueError):
                    print("Couldn't find cookie count or items")
        timeout = time() + wait_time
    if time() > five_min:
        # Get Cookie per minute
        try:
            per_sec = driver.find_element(By.ID, value="cookiesPerSecond")
            print(per_sec.text)
        except NoSuchElementException:
            print("No info")
        break

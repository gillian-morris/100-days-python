# Day 50 - Tindog Automate Swiping
# Automation on the web
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
from time import sleep

URL = os.environ["URL"]
ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 2)

login_btn = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn-tindog-login")))
login_btn.click()

login_bark_btn = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn-facebark")))
login_bark_btn.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email_input = wait.until(ec.presence_of_element_located((By.ID, "email")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, value="pass")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.click()

driver.switch_to.window(base_window)

allow = wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Allow"]')))
allow.click()

enable = wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="Not interested"]')))
enable.click()

accept = wait.until(ec.element_to_be_clickable((By.XPATH, '//button[text()="I Accept"]')))
accept.click()

for i in range(20):
    sleep(1)
    try:
        like_button = driver.find_element(By.CLASS_NAME, value='btn-like')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            sleep(2)
    except NoSuchElementException:
        sleep(2)

driver.quit()

# Day 52 - Share-a-Naan Bot
# A bot to follow users on a fictional social media
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import os

URL = "https://app.100daysofpython.dev/services/share-a-naan/"
ACCOUNT_EMAIL = "gamchihuahua@gmail.com"
ACCOUNT_PASSWORD = "VTynkPhwkWPORDwt"
account = "rordongamsay"

class NaanFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get(URL)
        sleep(2)

        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)

        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)

        submit_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()
        sleep(3)

        save_info = self.driver.find_elements(By.XPATH, "//div[contains(text(), 'Not now')]")
        if save_info:
            save_info[0].click()
        sleep(1)

        notifications = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Not Now')]")
        if notifications:
            notifications[0].click()
        sleep(2)

    def find_followers(self):
        self.driver.get(f"{URL}u/{account}/followers")
        sleep(2)
        popup_followers = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll" )
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup_followers)
            sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".followers-scroll button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
                cancel.click()

bot = NaanFollower()
bot.login()
bot.find_followers()
bot.follow()

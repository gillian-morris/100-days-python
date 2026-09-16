from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

URL = os.environ["URL"]
ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, "button.flex:nth-child(1)")
        go_btn.click()
        sleep(60)

        self.down = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/h3").text
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/h3").text

    def tweet_at_provider(self):
        self.driver.get(URL)
        sleep(2)

        email_input = self.driver.find_element(By.ID, "email")
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)

        password_input = self.driver.find_element(By.ID, value="password")
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)

        submit_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_btn.click()
        sleep(3)

        tweet_compose = self.driver.find_element(By.ID, "tweet-compose")
        tweet_compose.clear()
        tweet = f"Hey Innernet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}ip?"
        tweet_compose.send_keys(tweet)

        sleep(2)
        tweet_button = self.driver.find_element(By.ID, value='post-btn')
        tweet_button.click()

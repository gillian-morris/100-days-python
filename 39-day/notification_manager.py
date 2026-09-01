import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.phone = os.environ["Phone_NUM"]
        self.api = os.environ["Textbelt_API"]
        self.my_email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("MY_PASSWORD")

    def send_message(self, message_to_send):
        response = requests.post('https://textbelt.com/text', {
        "phone": self.phone,
        "message": message_to_send,
        "key": self.api,
        })
        print(response.json())

    def send_email(self, email_list, message):
        for email in email_list:
            full_message = "Subject:Low Flight\n\n" + message
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(
                        from_addr=self.my_email,
                        to_addrs=email,
                        msg=full_message)

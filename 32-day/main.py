# Day 32 - Birthday Wisher
# Sending emails via python script

import smtplib
import datetime as dt
import random
import pandas
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")
birthdays = df.to_dict(orient="records")

for birthday in birthdays:
    if now.month == birthday["month"] and now.day == birthday["day"]:
        letter_num = random.randint(1,3)
        letter = f"letter_templates/letter_{letter_num}.txt"
        with open(letter, "r") as f:
            letter_send = f.read()
        letter_send = letter_send.replace("[NAME]", birthday["name"].upper())
        message = "Subject:Happy Birthday!\n\n" + letter_send
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday["email"],
                    msg=message
                )

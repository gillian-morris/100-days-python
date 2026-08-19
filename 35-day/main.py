# Day 35 - Rainy SMS
# A python script that will send a text message using API Twilio and OpenWeatherMap to let you know if you need an umbrella that day.

import requests
import os
from twilio.rest import Client

OW_URL = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OW_API")
LAT = 35.871449,
LONG = -84.181671

RAIN_LAT = 43.547310
RAIN_LONG = -96.731300

parameters = {
    "lat": RAIN_LAT,
    "lon": RAIN_LONG,
    "appid": api_key,
    "cnt": 4
}

account_sid = os.environ.get("TWILIO_ACCOUNT")
auth_token = os.environ.get("TWILIO_TOKEN")
to_number = os.environ.get("TO_PHONE")
twilio_number = os.environ.get("TWILIO_NUM")

response = requests.get(OW_URL, params=parameters)
response.raise_for_status()
data = response.json()

is_raining = False
for weather in data["list"]:
    if weather["weather"][0]["id"] < 600:
        is_raining = True

if is_raining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_number,
        from_=twilio_number,
        body="sms_appointment_reminders",
    )

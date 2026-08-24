# Day 38 - Workout Tracking
# Using 100 days of code API and Google Sheets to track work outs.

import os
import requests
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEET_TOKEN = os.environ["SHEET_TOKEN"]

GENDER = os.environ["GENDER"]
WEIGHT_KG = os.environ["WEIGHT_KG"]
HEIGHT_CM = os.environ["HEIGHT_CM"]
AGE = os.environ["AGE"]

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_url = os.environ["SHEET_URL"]

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json',
}
parameters = {
    "query": input("Tell me the excercise you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}


response = requests.post(url, headers=headers, json=parameters)
response.raise_for_status()
data = response.json()

now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

sheet_header = {
    "Authorization": SHEET_TOKEN
}

for exercise in data["exercises"]:
    sheet_body = {
        "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(sheet_url, headers=sheet_header, json=sheet_body)
    response.raise_for_status()
    print(response.text)

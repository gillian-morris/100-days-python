import email

import requests
from dotenv import load_dotenv
import os

load_dotenv()
sheet1_URL = os.environ["SHEET_URL"] + "sheet1"
users_URL = os.environ["SHEET_URL"] + "users"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._authorization = {"Authorization": f"{os.environ["SHEET_AUTH"]}"}

        self.destination_data = {}
        self.customer_emails = []


    def get_flights(self):
        response = requests.get(sheet1_URL, headers=self._authorization)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_lowest_price(self, row_id, data):
        url_row = f"{sheet1_URL}/{row_id}"
        parameters = {
            "sheet1":{
                "lowestPrice": data.price
            }
        }
        requests.put(url=url_row, json=parameters, headers=self._authorization)
        if data.stops != "-1":
            return f"Low price alert! Only ${data.price} to fly from {data.origin_iata_code} to {data.dest_iata_code}, on {data.out_date} until {data.return_date}. The flight has {data.stops} layovers."
        else:
            return f"Low price alert! Only ${data.price} to fly from {data.origin_iata_code} to {data.dest_iata_code}, on {data.out_date} until {data.return_date}. The flight has 3 or more layovers."

    def get_customer_emails(self):
        response = requests.get(users_URL, headers=self._authorization)
        data = response.json()
        for user in data["users"]:
            self.customer_emails.append(user["email"])
        return self.customer_emails

import requests

from dotenv import load_dotenv
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = os.environ["SerpAPI_URL"]
        self._api_key = os.environ["SerpAPI_KEY"]

    def check_flights(self, origin_iata, destination_iata, from_time, to_time):
        self.body = {
            "engine":"google_flights",
            "api_key":self._api_key,
            "departure_id": origin_iata,
            "arrival_id": destination_iata,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "currency": "USD",
            "type": "1",
            "stops": "1",
        }
        self.response = requests.get(self.url, params=self.body)
        if "error" in self.response.json():
            self.body["stops"] = "1"
            self.response = requests.get(self.url, params=self.body)
            if "error" in self.response.json():
                self.body["stops"] = "2"
                self.response = requests.get(self.url, params=self.body)
                if "error" in self.response.json():
                    self.body["stops"] = "0"
                    self.response = requests.get(self.url, params=self.body)
        return self.response.json()

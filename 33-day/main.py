# Day 33 - ISS Overhead Notifier
# Working with APIs

from datetime import datetime, timezone
import requests

# Enter your latitude andn longitude
LATITUDE = 0
LONGITUDE = 0

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def check_position():
    if (
        iss_latitude - 5 <= LATITUDE
        <= iss_latitude + 5
        and iss_longitude - 5 <= LONGITUDE
        <= iss_longitude + 5
    ):
        return True

def is_night():
        if sunrise <= utc_time.hour or utc_time.hour <= sunset:
            return True


parameters = {"lat": LATITUDE, "lng": LONGITUDE, "formatted": 0}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

today = datetime.now()
utc_time = today.astimezone(timezone.utc)

if check_position() and is_night():
    print("The ISS is overhead!")
else:
    print("You could set up this code to run on loop and send an email when the ISS is overhead. Since this is sample code, I will leave it here. For an example of sending an email checkout day 32.")

# Day 47 - Automated Amazon Price Tracker
# Track prices of items on Amazon and alert when the price fall within desired price range.
# Something to expand this project create an excel with Sheety and pull information from there to do a check on more.

from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "update_website_here"
headers = "update_headers_here"

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price_div = soup.find(name="div", id="corePriceDisplay_desktop_feature_div")
price_span = price_div.find(name="span").text
price = float(price_span.replace("$",""))

# Set price to what you want
if price < 150:
    item_name = soup.find(name="h1", id="title")
    name = item_name.get_text(strip=True)

    message = f"{name} is now {price}"
    response = requests.post("https://textbelt.com/text",{
        "phone":os.environ["Phone_NUM"],
        "message": message,
        "key":os.environ["Textbelt_API"]
    })
    print(response.json())

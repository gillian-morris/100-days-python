# Day 36 - Stock Notifier
# Using APIs to send a text to notify changes of 5% or more in a stock with news information

import os
import requests
from datetime import datetime, timedelta
import requests_cache
from twilio.rest import Client

STOCK = "IBM"
COMPANY_NAME = "IBM"

STOCK_API = os.environ.get("STOCK_API")
NEWS_API = os.environ.get("NEWS_API")
account_sid = os.environ.get("twilio_account_sid")
auth_token = os.environ.get("twilio_auth_token")
to_number = os.environ.get("PHONE_NUM")
twilio_number = os.environ.get("TWILIO_NUM")

# Get yesterday and the day before
yesterday = datetime.now() - timedelta(days=1)
yesterday_str = f"{yesterday.year}-{yesterday.month:02d}-{yesterday.day:02d}"
day_before = datetime.now() - timedelta(days=2)

# URLs and parameters
stock_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API
}

news_params = {
    "qInTitle":COMPANY_NAME,
    "apiKey":NEWS_API

}
stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

# Cache API calls
requests_cache.install_cache('stock_cache')

# Stocks API call.
response = requests.get(stock_url, params=stock_params)
response.raise_for_status()
data = response.json()
# Calculate
yesterday_open = float(data["Time Series (Daily)"][f"{yesterday.year}-{yesterday.month:02d}-{yesterday.day:02d}"]["4. close"])
day_before_open = float(data["Time Series (Daily)"][f"{day_before.year}-{day_before.month:02d}-{day_before.day:02d}"]["4. close"])
open_diff = day_before_open - yesterday_open
diff_percent = (abs(open_diff) /yesterday_open) *100
# If number changes more that 5 we want a notification.
if diff_percent > 5:
    # Get news
    news_response = requests.get(news_url, news_params)
    news_response.raise_for_status()
    news_data = news_response.json()
    new_descript = []
    new_title = []
    # first three items and ad to list.
    for x in range(3):
        new_descript.append(news_data["articles"][x]["description"])
        new_title.append(news_data["articles"][x]["title"])
    # Send text message. Twilio does not allow for self formated bodies anymore.
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to_number,
        from_=twilio_number,
        body="sms_event_notifications",
    )

    if open_diff < 0:
        print(f"{STOCK}: 🔻{abs(int(open_diff))}%\n")
        for i in range(3):
            print(f"Header: {new_title[i]}")
            print(f"Brief: {new_descript[i]}")
    elif open_diff > 0:
        print(f"{STOCK}: 🔺{int(open_diff)}%\n")
        for i in range(3):
            print(f"Header: {new_title[i]}")
            print(f"Brief: {new_descript[i]}")

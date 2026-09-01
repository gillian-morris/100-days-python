# Day 39 & 40 Flight Deal Finder
# Using APIs to pull flight information and send messages for low price alerts.
#
from datetime import datetime, timedelta
import requests_cache
from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationManager

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 80000,
    },
)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6 * 365 / 12)

flight_data = DataManager()
sheet_flight_data = flight_data.get_flights()

lookup_flights = FlightSearch()
notification_manager = NotificationManager()

count = 0
for flight in sheet_flight_data:
    flight_info = lookup_flights.check_flights(
        "TYS", flight["iataCode"], tomorrow, six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flight_info, tomorrow, six_month_from_today)
    if cheapest_flight != "N/A":
        if int(cheapest_flight.price) < int(flight["lowestPrice"]):
            message = flight_data.update_lowest_price(count + 2, cheapest_flight)
            # notification_manager.send_message(message)
            notification_manager.send_email(flight_data.get_customer_emails(), message)
    count += 1

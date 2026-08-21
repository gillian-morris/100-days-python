# Day 37 - Habit Tracker
# A habit tracker with pixela, using get, post, put, delete

import os
from datetime import datetime
from time import strftime
import requests


TOKEN = os.environ.get("GRAPH_TOKEN")
USERNAME = os.environ.get("GRAPH_USERNAME")
GRAPH = os.environ.get("GRAPH_NAME")

# Create an account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "kuro",
}

headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Add pixel tracking
today = datetime.now()
today = today.strftime("%Y%m%d")

graph_name_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
post_pixel = {
    "date": today,
    "quantity": "15",
}
# response = requests.post(url=graph_name_endpoint, json=post_pixel, headers=headers)
# print(response.text)

# Update Pixel
graph_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today}"
quantity = {"quantity": "18"}
# response = requests.put(url=graph_update, json=quantity, headers=headers)
# print(response.text)

# Delete Info
# response = requests.delete(url=graph_update, headers=headers)
# print(response.text)

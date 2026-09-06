from bs4 import BeautifulSoup
import requests


class SongManager:
    def __init__(self):
        pass
    def get_top_songs(self, request_date):
        top_100 = "https://www.billboard.com/charts/hot-100/" + request_date
        response = requests.get(top_100)
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        songs = soup.find_all(name="ul", class_="o-chart-results-list-row")
        return [song.h3.get_text().strip("\n\t") for song in songs]

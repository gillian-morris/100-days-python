# Day 45 - Top 100 Movies
# A web scraping project to make a list of the top 100 movies of all time according to Variety 2022
from bs4 import BeautifulSoup
import requests

response =  requests.get("https://variety.com/lists/best-movies-of-all-time/the-graduate-1967-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies_name = soup.find_all(name="h2")
movie_list = [movie.get_text().split(" (")[0] for movie in movies_name]
movie_list = movie_list[:-2]
movie_list.reverse()

with open("movie_list.txt", "w") as file:
    for movie in movie_list:
        movie_num =  movie_list.index(movie) +1
        file.write(f"{movie_num}) {movie}\n")

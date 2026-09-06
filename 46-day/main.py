# Day 46 - Throwback Music Playlist
# Web scraping and API to make a little playlist

from song_manager import SongManager
from playlist_manager import PlaylistManager
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

song_manager = SongManager()

date = input("Which year do you want to travel to? Type the datein this format YYYY-MM-DD: ")
song_list = song_manager.get_top_songs(date)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ["SPOTIFY_CLIENT"],
        client_secret=os.environ["SPOTIFY_SECRET"],
        redirect_uri="https://example.com",
        scope="playlist-modify-private",))

spotify_track_list=[]
for song in song_list:
    query = f"track:{song}"
    results = sp.search(q=query, limit=1, type="track")
    items = results.get("tracks", {}).get("items", [])
    if items:
        track = items[0]
        spotify_track_list.append(track["uri"])
    else:
        print("No song found matching that query.")

playlist = sp.current_user_playlist_create(name=f"{date} Billboard 100",public=False,collaborative=False,description="Playlist with the top 100 songs from that week")
sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_track_list)

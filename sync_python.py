import spotipy
from spotipy.oauth2 import SpotifyOAuth
import ytmusicapi
import json

#Loading the JSON with user credentials for both services
user_file = open("credentials.json")
user_data = json.load(user_file)
user_file.close()


#Setting the spotify side of things
spotify_client_id = user_data["user_credentials"][0]["spotify_client_id"]
spotify_key = user_data["user_credentials"][0]["spotify_client_secret"]
spotify_playlist = user_data["user_credentials"][0]["spotify_playlist_key"]
script_scope = "user-library-read"
user_session = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=script_scope))


import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import ytmusicapi
import json

#Loading the JSON with user credentials for both services
user_file = open("credentials2.json")
user_data = json.load(user_file)
user_file.close()


#Setting the spotify side of things
spotify_client_id = user_data["user_credentials"][0]["spotify_client_id"]
spotify_key = user_data["user_credentials"][0]["spotify_client_secret"]
spotify_redirect_uri = user_data["user_credentials"][0]["spotify_redirect_uri"]
spotify_playlist = user_data["user_credentials"][0]["spotify_playlist_key"]

print(f"client id: {spotify_client_id} \n client secret: {spotify_key}")


os.environ["SPOTIPY_CLIENT_ID"] = spotify_client_id
os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_key
os.environ["SPOTIPY_REDIRECT_URI"] = spotify_redirect_uri

spotipy.oauth2.SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_key)

script_scope = "user-library-read"
user_session = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=script_scope))

results = user_session.current_user_saved_tracks(limit=20)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])


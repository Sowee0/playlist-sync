import os
import json
# import spotipy
from ytmusicapi import YTMusic
# from spotipy.oauth2 import SpotifyOAuth


def getArtists(track):
    artists = ""

    for artist in track['artists']:
        artists += artist['name']
        artists += " "

    return artists


def getVideoIdForTrack(track):
    query = track['title'] + " "
    artists = getArtists(track)
    query += artists

    searchResults = ytmusic.search(
        ignore_spelling=True, query=query, limit=int(1), filter="songs")

    return searchResults[0]['videoId']


ytmusic = YTMusic('headers_auth.json')
playlist = ytmusic.get_playlist('PLKPa_-QZ5p9Xh9eqwR1op3YCpmJCXhdC1')

for track in playlist['tracks']:
    print(getVideoIdForTrack(track))


# json_formatted_str = json.dumps(playlist['tracks'], indent=2)


""" #Loading the JSON with user credentials for both services
user_file = open("credentials2.json")
user_data = json.load(user_file)
user_file.close()


# Setting the spotify side of things
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

 """

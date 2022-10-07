import os
import json
from re import search
import spotipy
from ytmusicapi import YTMusic
from difflib import SequenceMatcher
from spotipy.oauth2 import SpotifyOAuth

ytmusic = YTMusic('headers_auth.json')
playlist = ytmusic.get_playlist('PLKPa_-QZ5p9Xh9eqwR1op3YCpmJCXhdC1')


def getYtmArtists(track):
    artists = ""

    for artist in track['artists']:
        artists += artist['name']
        artists += " "

    return artists


def getYtmTrackInfo(track):
    query = track['title'] + " "
    artists = getYtmArtists(track)
    query += artists

    searchResults = ytmusic.search(
        ignore_spelling=True, query=query, limit=int(1), filter="songs")

    if len(searchResults) >= 1 and 'videoId' in searchResults[0]:
        artistName = ""
        for artist in searchResults[0]['artists']:
            artistName = artistName + " " + artist['name']

        return dict(
            id=searchResults[0]['videoId'],
            artist=artistName,
            title=searchResults[0]['title'],
            service="ytm"
        )

    return False


def getYtmTracks():
    tracks = []

    for track in playlist['tracks']:
        trackInfo = getYtmTrackInfo(track)

        if trackInfo:
            tracks.append(trackInfo)

    return tracks

##################################################################################################################################

############################################################# SPOTIFY ############################################################


##################################################################################################################################
# json_formatted_str = json.dumps(playlist['tracks'], indent=2)
# Loading the JSON with user credentials for both services
user_file = open("credentials.json")
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
script_scope = "user-library-read"

spotipy.oauth2.SpotifyClientCredentials(
    client_id=spotify_client_id, client_secret=spotify_key
)

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=script_scope
    )
)


def getSpotifyArtists(track):
    artists = ""

    for artist in track['artists']:
        artists += artist['name']
        artists += " "

    return artists


def getSpotifyTrackInfo(track):
    trackName = track['name']
    trackArtists = getSpotifyArtists(track)

    return dict(
        id=track['id'],
        artist=trackArtists,
        title=trackName,
        service="spotify"
    )


def getSpotifyTracks():
    results = spotify.playlist(spotify_playlist)

    tracks = []

    for _, item in enumerate(results['tracks']['items']):
        track = item['track']

        trackInfo = getSpotifyTrackInfo(track)

        tracks.append(trackInfo)

    return tracks


def similarStrings(a, b):
    return SequenceMatcher(None, a, b).ratio() >= 0.8


def hasSimilarInOtherList(trackName, trackList):
    hasSimilar = False

    for track in trackList:
        if similarStrings(track['title'], trackName):
            hasSimilar = True

    return hasSimilar


def getMissingTracks(ytmTracks, spotifyTracks):
    missingTracks = []

    for track in ytmTracks:
        if not hasSimilarInOtherList(track['title'], spotifyTracks):
            missingTracks.append(track)

    for track in spotifyTracks:
        if not hasSimilarInOtherList(track['title'], ytmTracks):
            missingTracks.append(track)

    return missingTracks


def getSpotifyTrackId(track):
    spotifyTrackId = False

    searchResult = spotify.search(
        q="artist:"+track['artist']+" track:"+track['title'], limit=1)

    if searchResult['tracks'] and len(searchResult['tracks']['items']) > 0:
        spotifyTrackId = searchResult['tracks']['items'][0]['id']

    return spotifyTrackId


def getYtmTrackId(track):
    query = track['title'] + " " + track['artist']

    searchResults = ytmusic.search(
        ignore_spelling=True, query=query, limit=int(1), filter="songs")

    if len(searchResults) >= 1 and 'videoId' in searchResults[0]:
        artistName = ""
        for artist in searchResults[0]['artists']:
            artistName = artistName + " " + artist['name']

        return searchResults[0]['videoId']

    return False

def addToSpotify(tracks):
    spotify.playlist_add_items(playlist_id=spotify_playlist, items=tracks)

def addToYtm(tracks):
    YTMusic.add_playlist_items(playlistId=ytm_playlist, videoIds=tracks)



def run():
    ytmTracks = getYtmTracks()
    spotifyTracks = getSpotifyTracks()
    missingTracks = getMissingTracks(ytmTracks, spotifyTracks)

    newTracksSpotify = []
    newTracksYtm = []

    for track in missingTracks:
        if track['service'] == 'spotify':
            trackId = getSpotifyTrackId(track)

            if trackId:
                newTracksSpotify.append(trackId)

        if track['service'] == 'ytm':
            trackId = getYtmTrackId(track)

            if trackId:
                newTracksYtm.append(trackId)

    if(len(addToSpotify)):
        addToSpotify(newTracksSpotify)

    if(len(addToYtm)):
        addToYtm(newTracksYtm)

    print(f"Added to spotify: {newTracksSpotify}")
    print(f"Added to ytm: {newTracksYtm}")


run()

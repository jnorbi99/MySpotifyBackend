import json
import requests
from requests.api import post
import create_playlist
import details
import search_track

PLAYLIST_URL = details.SPOTIFY_CREATE_PLAYLIST_URL + "/" + create_playlist.MYID + "/tracks"
AUTH_TOKEN = details.AUTH_TOKEN
MY_URI = "spotify:track:" + search_track.SONG_ID

def add_item_to_playlist(position, uris):
    response = requests.post(
        PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {AUTH_TOKEN}"
        },
        json={
            "position": position,
            "uris": uris
        }
    )
    json_resp = response.json()
    return json_resp

def add():
    add_item_to_playlist(
        position = 0,
        uris = [MY_URI])

add()
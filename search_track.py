import requests
import json

AUTH_TOKEN = "my_token_2"
SEARCH_URL = "https://api.spotify.com/v1/search"
MY_SEARCH = "MYSEARCH"

def search_track(type):
    response = requests.get(
        SEARCH_URL + "?q=" + MY_SEARCH + "&type=" + type,
        headers={
            "Authorization": f"Bearer {AUTH_TOKEN}"
        },
    )
    json_resp = response.json()
    return json_resp

def search():
    
    s = search_track(
        type = "track"
    )   
    songId = s["tracks"]["items"][0]["id"]
    return songId  

SONG_ID = search()
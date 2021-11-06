import requests
import details

SPOTIFY_CREATE_PLAYLIST_URL = details.SPOTIFY_CREATE_PLAYLIST_URL
AUTH_TOKEN = details.AUTH_TOKEN

def create_playlist(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {AUTH_TOKEN}"
        },
        json={
            "name" : name,
            "public" : public
        }
    )
    json_resp = response.json()
    return json_resp

def create() :
    playlist = create_playlist(
        name = "My first try",
        public = False
    )
    id = playlist["external_urls"]["spotify"][-22:]
    return id

MYID = create()





from dotenv import load_dotenv
import requests
import os
from random import randrange



# obtenir des informations sur un artiste
def get_artiste(artist_name: str):
    res = requests.get(os.getenv("URL_ARTISTE") + artist_name)
    #idArtist = res.json()
    return (res.json(), res.status_code)

# obtenir un album au hazard
def get_random_album(artist_name: str):
    id_artist = get_artiste(artist_name)[0]['artists'][0]['idArtist']  
    res = requests.get(os.getenv("URL_ALBUM") + id_artist)
    album = res.json()['album']
    m = randrange(0, len(album))
    return (album[m], res.status_code)

# obtenir un track et une video au hazard
def get_random_track(artist_name: str):
    id_album = get_random_album(artist_name)[0]["idAlbum"]
    res = requests.get(os.getenv("URL_TRACK") + id_album)
    track = res.json()['track']
    m = randrange(0, len(track))
    songs = {}
    songs ['artist'] = track[m]["strArtist"]
    songs['title'] = track[m]["strTrack"]
    songs['suggested_youtube_url']=track[m]["strMusicVid"]
    return (songs, res.status_code)
 



if __name__ == "audiodb":
    load_dotenv()
    




from dotenv import load_dotenv
import requests
import os
from random import randrange
import json

load_dotenv()


# obtenir des informations sur un artiste
def get_artiste(artist_name: str):
    res = requests.get(os.getenv("url_artiste") + artist_name)
    return res.json()

# obtenir  des informations sur une musique au hazard

# obtenir des informations sur un album

# obtenir un album au hazard
def get_random_album(artist_name: str):
    id_artist = get_artiste(artist_name)['artists'][0]['idArtist']
    res = requests.get(os.getenv("url_album") + id_artist)
    album = res.json()['album']
    m = randrange(0, len(album))
    return album[m]

# obtenir un track au hazard
def get_random_track(artist_name: str):
    id_album = get_random_album(artist_name)["idAlbum"]
    res = requests.get(os.getenv("url_track") + id_album)
    track = res.json()['track']
    m = randrange(0, len(track))
    songs = {}
    songs ['artist'] = track[m]["strArtist"]
    songs['title'] = track[m]["strTrack"]
    return songs 
 
# obtenir une video au hazard

def get_random_video(artist_name: str):
    id_artist = get_artiste(artist_name)['artists'][0]['idArtist']
    res = requests.get(os.getenv("url_video") + id_artist)
    video = res.json()['mvids']
    if video == None:
        return video 
    else:
        m = randrange(0, len(video))
        return video[m]["strMusicVid"]

# a=get_random_video(artist_name='Tryo')
# print(a)








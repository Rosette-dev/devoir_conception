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
    # id_artist = get_artiste(artist_name)['artists'][0]['idArtist']
    id_album = get_random_album(artist_name)["idAlbum"]
    res = requests.get(os.getenv("url_track") + id_album)
    track = res.json()['track']
    m = randrange(0, len(track))
    return track[m]   # voir la possibilité de récupérer que des info interesssantes

# obtenir une video au hazard

def get_random_video(artist_name: str):
    id_artist = get_artiste(artist_name)['artists'][0]['idArtist']
    res = requests.get("https://theaudiodb.com/api/v1/json/2/mvid.php?i=" + id_artist)
    video = res.json()['mvids']
    m = randrange(0, len(video))
    return video[m]

# a=get_random_track(artist_name='Technotronic')
# print(a)








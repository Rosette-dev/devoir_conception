from dotenv import load_dotenv
import os
import json
import requests
from random import randrange

load_dotenv()

def getname():
    data=json.load(open(os.getenv("CLIENT_DATA")))
    artist=[]
    for i in range(len(data)):
        artist.append(data[i]["artiste"])
    return artist

liste_artiste=getname()


def get_playlists(liste_artiste):
    playlist = dict()
    for i in range(20):
        step = randrange(0, len(liste_artiste))
        artist_name = liste_artiste[step]
        r = requests.get(os.getenv("url_service") + "/random/" + artist_name)
        playlist[i] = r.json()
    return playlist # vérifier les lyrics 
# avant de sortir la playlist

r = get_playlists(liste_artiste)
print(r) 

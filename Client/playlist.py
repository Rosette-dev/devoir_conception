from dotenv import load_dotenv
import os
import json
import requests
from random import randrange


def getname():
    data=json.load(open(os.getenv("CLIENT_DATA")))
    artist=[]
    for i in range(len(data)):
        artist.append(data[i]["artiste"])
    return artist


def get_playlists(liste_artiste):
    """Mise en place du scénario client
    Args:
        liste_artiste (str): la liste des noms des artistes obtenue à partir du json

    Returns:
        playlist (dict): une playliste aléatoire basée sur le json
    """
    playlist = dict()
    for i in range(20):
        step = randrange(0, len(liste_artiste))
        artist_name = liste_artiste[step]
        r = requests.get(os.getenv("URL_SERVICE") + "/random/" + artist_name).json()
        playlist[i] = r['lyrics']
    return playlist 


if __name__ == "playlist":
    load_dotenv()
import requests
import os
from audiodb import get_random_track


def get_lyrics(artist_name):
    track = get_random_track(artist_name)
    title = track['strTrack']
    res = requests.get(os.getenv("url_lyric") + artist_name + "/" + title)
    return res.json()

a=get_lyrics(artist_name='Bob Marley')
print(a)

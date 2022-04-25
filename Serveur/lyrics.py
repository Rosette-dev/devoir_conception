from dotenv import load_dotenv
import requests
import os
from audiodb import get_random_track, get_random_video


def get_lyrics(artist_name):
    songs = get_random_track(artist_name)
    songs["suggested_youtube_url"] = get_random_video(artist_name)
    res = requests.get(os.getenv("url_lyric") + artist_name + "/" + songs["title"])
    if res.status_code == 200:
        songs["lyrics"] = res.json()
    return songs
    # while res.status_code != 200: 
    #     res = requests.get(os.getenv("url_lyric") + artist_name + "/" + songs["title"])
    # songs["lyrics"] = res.json()
    # return songs
        
 
# a=get_lyrics(artist_name='Technotronic')
# print(a)

from dotenv import load_dotenv
import requests
import os
from audiodb import get_random_track, get_random_video


def get_lyrics(artist_name):
    """Retourne les lyrics d'une chanson ainsi que le status de la requête de 
    l'api LyricsOvh
    """
    songs = get_random_track(artist_name)[0]
    songs["suggested_youtube_url"] = get_random_video(artist_name)[0]
    res = requests.get(os.getenv("URL_LYRIC") + artist_name + "/" + songs["title"])
    if res.status_code == 200:
        songs["lyrics"] = res.json()
    else:
        songs["lyrics"] = None
    return (songs,res.status_code)

        
 


if __name__ == "__lyrics__":
    load_dotenv()
    

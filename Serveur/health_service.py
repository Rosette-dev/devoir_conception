from audiodb import *
from lyrics import *

def audiodb_artiste_condition():
    """Retourne le status de la requète de l'Api Audiodb 
    pour obtenir l'identifiant d'un artiste
    """
    res = get_artiste(artist_name="oasis")
    return {"health_audiodb_get_artiste": res[1]}

def audiodb_album_condition():
    """Retourne le status de la requète de l'Api Audiodb 
    pour obtenir un album d'un artiste
    """
    res= get_random_album(artist_name= 'oasis')
    return {"health_audiodb_album": res[1]}


def audiodb_track_condition():
    """Retourne le status de la requète de l'Api Audiodb 
    pour obtenir une chanson d'un artiste
    """
    res= get_random_track(artist_name= 'oasis')
    return {"health_audiodb_track": res[1]}

def audiodb_video_condition():
    """Retourne le status de la requète de l'Api Audiodb 
    pour obtenir la vidéo d'une chanson d'un artiste
    """
    res= get_random_video(artist_name= 'oasis')
    return {"health_audiodb_video": res[1]}

def lyrics_condition():
    """Retourne le status de la requète de l'Api LyricsOvh 
    pour obtenir les lyrics d'une chanson d'un artiste
    """
    res= get_lyrics(artist_name= 'oasis')
    return {"health_lyrics": res[1]}




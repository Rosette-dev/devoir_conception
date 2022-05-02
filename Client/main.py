from playlist import *
import json


# Création d'une playliste de 20 chansons aléatoires
Playlist = get_playlists(liste_artiste=getname())
# récupération des lyrics dans le fichier Playlist
with open("Playlist.json","w") as outfile:
    json.dump(Playlist, outfile)
    
#print(json.dumps(Playlist,indent=4))

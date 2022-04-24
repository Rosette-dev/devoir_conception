import os
import json
import random
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
import requests

load_dotenv()

app = FastAPI()
@app.get("/")
async def root():
    return ["message", "Hello World"]

# def album():
#     res=requests.get("https://theaudiodb.com/api/v1/json/2/album.php?i=112884")
#     return res.json()


# a=album() 
# print(a)
#os.getenv("urlaudiodb")
#os.getenv("urlalbum")+"Tryo"


# @app.get("/random/{artist_name}")
# async def get_playlist(artist_name):
#     artist= artist_name
#     return album(artist)


#supposer que j'ai la liste des titre de l'artiste
@app.get("/{artist_name}")
async def get_playlist(artist_name):
    res1=requests.get(os.getenv("url_artiste"))
    id=res1.json()#{"artists": [0]}
    idArtist=id['artists'][0]['idArtist']

    res2= requests.get(os.getenv("url_music")+idArtist)
 

    # title=random.choice(liste_title)
    # res3=requests(urllyrics)
    return res.json() # res.json()

# def test():
#     res2= requests.get(os.getenv("url_music")+"118294")
#     id=res2.json()
#     return id 
    
# a=test()
# #print(a.keys())
# print(a)





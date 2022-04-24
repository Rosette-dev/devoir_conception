from dotenv import load_dotenv
import os
import json
import requests
#from pydantic import BaseModel

load_dotenv()

def getname():
    data=json.load(open(os.getenv("CLIENT_DATA")))
    artist=[]
    for i in range(len(data)):
        artist.append(data[i]["artiste"])
    return artist

liste_artiste=getname()
#for j in range(len(liste_artiste)):

#r=requests.get("http://127.0.0.1:8000/random/"+ str(liste_artiste[5]))
r=requests.get("http://127.0.0.1:8000")
print(r.json())

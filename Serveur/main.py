import os
import json
import random
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
import requests
from lyrics import get_lyrics
load_dotenv()

app = FastAPI()
@app.get("/")
async def root():
    return ["message", "Hello World"]






@app.get("/random/{artist_name}")
async def get_playlist(artist_name):
    res = get_lyrics(artist_name)
    return res.json()








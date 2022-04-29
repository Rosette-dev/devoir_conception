import os
# import json
# import random
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
# import requests
from lyrics import get_lyrics


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/random/{artist_name}")
async def get_playlist(artist_name):
    res = get_lyrics(artist_name)
    return res



if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="localhost", port=int(os.getenv("TARGET_PORT")))






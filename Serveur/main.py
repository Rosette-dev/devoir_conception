import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from lyrics import get_lyrics
from audiodb import *
from health_service import *
from fastapi import FastAPI
from fastapi_health import health

app = FastAPI()


app.add_api_route("/", health([audiodb_artiste_condition, audiodb_album_condition, 
                                       audiodb_track_condition,audiodb_video_condition,lyrics_condition ]))



@app.get("/random/{artist_name}")
async def get_playlist(artist_name):
    res = get_lyrics(artist_name)
    return res[0]


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=int(os.getenv("TARGET_PORT")))


#uvicorn main:app --reload



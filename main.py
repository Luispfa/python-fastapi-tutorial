from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(
    title='FastApi FitCoding!!!',
    description='API tutorial con documentación personalizada',
    version='1.0.0',
    contact={
        'name': 'FitCoding Team',
        'email': 'contacto@email.com' 
    }
)

songs = [
    {
        "id": 1,
        "title": "Bohemian Rhapsody",
        "artist": "Queen",
        "year": 1975,
        "genre": "Rock",
        "duration": "5:55"
    },
    {
        "id": 2,
        "title": "Shape of You",
        "artist": "ed Sheeran",
        "year": 2017,
        "genre": "Pop",
        "duration": "3:53"
    }
]

class Song(BaseModel):
    id: int | None = None
    title: str
    artist: str
    year: int
    genre: str
    duration: str
    

@app.get(
    "/",
    tags=['Home'],
    summary='Welcome Endpoint',
    description='Returns a personalized welcome message.',
    response_description='Welcome message in HTML format.'
)
def home():
    return HTMLResponse("<h1>Hello world!!</h1>")

@app.get(
    "/songs",
    tags=['Songs'],
    summary='Get all songs.',
    description='Returns a list of all available songs.',
    response_description='List of songs in JSON format.',
    response_model=List[Song]
)
def get_songs():
    return songs

@app.get(
    "/songs/{id}",
    tags=['Songs'],
    summary='Get song by ID.',
    description='Returns a specific song based on its ID.',
    response_description='Details of the song in JSON format. Returns a 404 error.',
    response_model=Optional[Song]
)
def get_song(id: int):
    for song in songs:
        if song['id'] == id:
            return song
        
    raise HTTPException(status_code=404, detail='Song not found.')

@app.get(
    "/songs/",
    tags=['Songs'],
    summary='Get song by genre and year.',
    description='Returns a song that matches the specified gender and year.',
    response_description='Details of the song in JSON format. Returns a 404 error.',
    response_model=Song
)
def get_song_by_genre(genre: str, year: int):
    for song in songs:
        if song['genre'] == genre:
            return song
        
    raise HTTPException(status_code=404, detail='Song not found.')

@app.post(
    "/songs",
    tags=['Songs'],
    summary="Insert a new song into the list.",
    description="Adds a new song to the in-memory list using the provided details like title, artist, year, genre, and duration.",
    response_description="The newly added song in JSON format.",
    response_model=List[Song],
    status_code=201
)
def create_song(song: Song):
    new_id= len(songs) + 1
    
    new_song = song.model_dump()
    new_song["id"] = new_id
    
    songs.append(new_song)
    
    return songs
    
    



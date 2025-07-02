from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

songs = [
    {"id": 1, "title": "Bohemian Rhapsody", "artist": "Queen", "year": 1975, "genre": "Rock", "duration": "5:55"},
    {"id": 2, "title": "Shape of You", "artist": "ed Sheeran", "year": 2017, "genre": "Pop", "duration": "3:53"}
]

class Song(BaseModel):
    id: int | None = None
    title: str
    artist: str
    year: int
    genre: str
    duration: str

# --- Create an APIRouter for all CRUD routes ---
# We set a '/songs' prefix so that all routes here start with /songs
router = APIRouter(prefix="/songs", tags=["Songs CRUD"])

@router.get(
    "", # The path will be /songs
    summary='Get all songs.',
    description='Returns a list of all available songs.',
    response_description='List of songs in JSON format.',
    response_model=List[Song]
)
def get_songs():
    return songs

@router.get(
    "/{id}", # The path will be /songs/{id}
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

@router.get(
    "/", # The path will be /songs/?genre=Rock&year=1957
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

@router.post(
    "",
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

# yuo can add PUT, DELETE, etc.
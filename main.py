from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List

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
    response_description='List of songs in JSON format.'
)
def get_songs() -> List[dict]:
    return songs
from fastapi import FastAPI, HTTPException
from enum import Enum


app = FastAPI()

class GenreURLChoices(Enum):
     ROCK = "rock"
     ELECTRONIC = "electronic"
     METAL = "metal"
     HIP_HOP = "hip-hop"



BANDS = [
  {"id" : 1, "name" : "The Kinks" , "genre" : "Rock"},    
  { "id": 2, "name": "The Beatles", "genre": "Rock" },
  { "id": 3, "name": "Pink Floyd", "genre": "Hip-hop" },
  { "id": 4, "name": "The Rolling Stones", "genre": "Metal" },
  { "id": 5, "name": "Led Zeppelin", "genre": "Rock" },
  { "id": 6, "name": "Queen", "genre": "Electronic" }
]



@app.get('/bands')
async def bands() -> list:
    return BANDS


@app.get('/bands/{band_id}', status_code=200) 
async def band(band_id : int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band with this id not found")
    return band
    

@app.get('/bands/genre/{genre}', status_code=200)
async def bands_for_genre(genre : GenreURLChoices) -> list[dict]:
      return [
           b for b in BANDS if b['genre'].lower() == genre.value
      ]
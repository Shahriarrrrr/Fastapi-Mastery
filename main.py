from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, Band


app = FastAPI()




BANDS = [
  {"id" : 1, "name" : "The Kinks" , "genre" : "Rock"},    
  { "id": 2, "name": "The Beatles", "genre": "Rock" },
  { "id": 3, "name": "Pink Floyd", "genre": "Hip-hop" },
  { "id": 4, "name": "The Rolling Stones", "genre": "Metal" , 'albums' : [
       {'title' : 'Master of Reality', 'release_date' : '1971-07-21'}
  ]},
  { "id": 5, "name": "Led Zeppelin", "genre": "Rock" },
  { "id": 6, "name": "Queen", "genre": "Electronic" }
]



@app.get('/bands')
async def bands() -> list[Band]:
    return [
         Band(**b) for b in BANDS
    ]



@app.get('/bands/{band_id}', status_code=200) 
async def band(band_id : int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Band with this id not found")
    return band
    


@app.get('/bands/genre/{genre}', status_code=200)
async def bands_for_genre(genre : GenreURLChoices) -> list[dict]:
      return [
           b for b in BANDS if b['genre'].lower() == genre.value
      ]
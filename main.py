from fastapi import FastAPI


app = FastAPI()

BANDS = [
  { "id": 2, "name": "The Beatles", "genre": "Rock" },
  { "id": 3, "name": "Pink Floyd", "genre": "Progressive Rock" },
  { "id": 4, "name": "The Rolling Stones", "genre": "Blues Rock" },
  { "id": 5, "name": "Led Zeppelin", "genre": "Hard Rock" },
  { "id": 6, "name": "Queen", "genre": "Classic Rock" }
]



@app.get('/bands')
async def bands() -> list:
    return BANDS


@app.get('/about')
async def about() -> str:
    return "An exceptional Company"
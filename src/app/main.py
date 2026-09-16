from fastapi import FastAPI, HTTPException
import app.utils.helpers as helpers
from app.settings import settings

items = helpers.create_sample_items()

# Only serve the API docs in non production environment
app = FastAPI(
    docs_url=None if settings.is_production else "/docs",
    redoc_url=None if settings.is_production else "/redoc",
    openapi_url=None if settings.is_production else "/openapi.json"
)

@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.get("/items/random")
def get_random_item():
    return items[helpers.randomise(0, len(items)-1)]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Checking if item_id is out of range
    if item_id < 1 or item_id > len(items):
        raise HTTPException(status_code=404, detail ="Item not found")

    return items[item_id-1]

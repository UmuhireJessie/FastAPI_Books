from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    "book1": {"title": "title1", "author": "Author One"},
    "book2": {"title": "titl2", "author": "Author Two"},
    "book3": {"title": "title3", "author": "Author Three"},
    "book4": {"title": "title4", "author": "Author Four"},
    "book5": {"title": "title5", "author": "Author Five"},
}

class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
    return {"Direction": direction_name, "sub": "Right"}


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_tiile": book_id}




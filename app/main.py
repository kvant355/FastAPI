from fastapi import FastAPI
from utils_my import get_book_from_library


app = FastAPI()

@app.get("/library/book/{book_id}/status")
def get_book(book_id: int):
    return get_book_from_library(book_id)
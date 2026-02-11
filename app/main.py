from fastapi import FastAPI, HTTPException, status
from typing import List
from app.schemas import BookCreate, BookResponse
from app.repository import BookRepository
from app.service import BookService

app = FastAPI(title="Book Library API", version="1.0.0")

repository = BookRepository()
service = BookService(repository)


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def add_book(book: BookCreate):
    created_book = service.add_book(book)
    return created_book


@app.get("/books", response_model=List[BookResponse])
def list_books():
    books = service.get_all_books()
    return books


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    book = service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    deleted = service.delete_book(book_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with id {book_id} not found"
        )
    return None
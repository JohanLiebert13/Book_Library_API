from typing import List, Optional
from app.repository import BookRepository
from app.models import Book
from app.schemas import BookCreate


class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def add_book(self, book_data: BookCreate) -> Book:
        return self.repository.create(
            title=book_data.title,
            author=book_data.author,
            year=book_data.year,
            genre=book_data.genre
        )

    def get_all_books(self) -> List[Book]:
        return self.repository.get_all()

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.repository.get_by_id(book_id)

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete(book_id)
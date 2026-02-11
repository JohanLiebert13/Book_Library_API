from typing import Dict, Optional, List
from app.models import Book


class BookRepository:
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.next_id: int = 1

    def create(self, title: str, author: str, year: int, genre: Optional[str] = None) -> Book:
        book = Book(
            id=self.next_id,
            title=title,
            author=author,
            year=year,
            genre=genre
        )
        self.books[self.next_id] = book
        self.next_id += 1
        return book

    def get_all(self) -> List[Book]:
        return list(self.books.values())

    def get_by_id(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id)

    def delete(self, book_id: int) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
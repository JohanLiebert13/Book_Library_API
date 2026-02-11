from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    genre: Optional[str] = None
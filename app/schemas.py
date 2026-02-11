from pydantic import BaseModel, Field
from typing import Optional


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    year: int = Field(..., gt=0)
    genre: Optional[str] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: Optional[str] = None

    class Config:
        from_attributes = True
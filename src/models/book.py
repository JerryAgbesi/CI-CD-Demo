from typing import Optional
from pydantic import BaseModel,Field

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    isbn: str

    class Config:
        from_attributes = True
   

class BookCreate(BaseModel):
    title: str = Field(...)
    author: str  = Field(...)
    isbn: str  = Field(...)
    
class BookUpdate(BaseModel):
    title: Optional[str]
    author: Optional[str]
    isbn: Optional[str]



   
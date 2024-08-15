
from typing import Optional
from pydantic import BaseModel,Field


class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


    class Config:
        from_attributes = True
   

class UserCreate(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)

class UserUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]


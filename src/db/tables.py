from .database import Base

from sqlalchemy import Column,Integer,String,ForeignKey,TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,unique=True,index=True)
    created_at = Column(TIMESTAMP,default=datetime.now())

    books = relationship("Book", back_populates="reader")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    author = Column(String,nullable=False)
    isbn = Column(String,nullable=False)
    created_at = Column(TIMESTAMP,default=datetime.now())

    reader_id = Column(Integer,ForeignKey("users.id"))

    reader = relationship("User",back_populates="books")


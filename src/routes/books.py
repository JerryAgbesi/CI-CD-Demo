from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
import logging

from ..db.database import get_db
from ..models.book import BookModel,BookCreate,BookUpdate
from ..db.tables import Book

logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

appRouter = APIRouter(prefix="/books", tags=["books"])


@appRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=BookModel)
def create_book(student:BookCreate ,db: Session = Depends(get_db)):
    new_book = Book(**student.model_dump())
    try:
        db.add(new_book)
        db.commit()
        db.refresh(new_book)

        logging.info("new book created")
        
        return new_book
    except Exception as e:
        db.rollback()
        logging.debug(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Unable to create book")
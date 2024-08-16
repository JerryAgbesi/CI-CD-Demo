from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
import logging

from ..db.database import get_db
from ..models.book import BookModel,BookCreate,BookUpdate
from ..db.tables import Book

logging.basicConfig(format='%(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

appRouter = APIRouter(prefix="/books", tags=["books"])


@appRouter.post("/",status_code=status.HTTP_201_CREATED,response_model=BookModel)
def create_book(book:BookCreate ,db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
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

@appRouter.get("/{book_id}",status_code=status.HTTP_200_OK,response_model=BookModel)
def get_book(book_id:int,db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    
    return book

@appRouter.patch("/{book_id}",status_code=status.HTTP_200_OK,response_model=BookModel)
def update_book(book_id:int,book:BookUpdate,db: Session = Depends(get_db)):
    get_book =  db.query(Book).filter(Book.id == book_id)
    get_book_object = get_book.first()
    if not get_book_object:
        raise HTTPException(status_code=404,detail="book not found")
    

    
    update_data = book.model_dump(exclude_unset=True)
    # new_update = {k: v for k, v in update_data.items() if v is not None}

    for key, value in update_data.items():
        setattr(get_book_object,key,value)  
    
    # get_book.update(new_update)
    
    
    db.commit()

    return get_book.first()

@appRouter.delete("/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id:int,db: Session = Depends(get_db)):
    get_book =  db.query(Book).filter(Book.id == book_id)
    if not get_book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    
    get_book.delete(synchronize_session=False)
    db.commit()
    return None
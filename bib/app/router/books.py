from app import crud
from app.dependency import get_db
from app.schemas import BookCreate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate, db: Session = Depends(get_db)
):  # db: Session = Depends(get_db) - fastapi вызывает get_db(), создаёт Session (подключение к БД), передаёт его в db
    return crud.create_book(db, book)


@router.put("/{book_id}")
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id, book)

    if not updated_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    delete_book = crud.delete_book(db, book_id)

    if not delete_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    return update_book

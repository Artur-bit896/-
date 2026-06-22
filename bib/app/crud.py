from app import models, schemas
from sqlalchemy.orm import Session


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author)

    db.add(db_book)  # Добавляем в Session
    db.commit()  # Cохраняем объект
    db.refresh(db_book)  # обновляем объект

    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()


def get_book(db: Session, book_id):
    return db.query(models.Book).filter(models.Book.id == book_id).first() # .first нужен чтобы запрос отправился в бд


def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    book = (
        db.query(models.Book).filter(models.Book.id == book_id).first()
    )  # first возвращает первый объект или ничего а не все как all

    if not book:
        return None

    book.title = updated_book.title
    book.author = updated_book.author

    db.commit()
    db.refresh(book)

    return book


def delete_book(db: Session, book_id: int):
    book = (
        db.query(models.Book).filter(models.Book.id == book_id).first()
    )  # first возвращает первый объект или ничего а не все как all

    if not book:
        return None

    db.delete(book)
    db.commit()

    return "This book is deleted"


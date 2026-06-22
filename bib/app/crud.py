from app import models, schemas
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Book


async def create_book(db: AsyncSession, book: schemas.BookCreate):
    db_book = models.Book(title=book.title, author=book.author)

    db.add(db_book)  # Добавляем в Session
    db.commit()  # Cохраняем объект
    db.refresh(db_book)  # обновляем объект

    return db_book


async def get_books(db: AsyncSession):
    result = await db.execute(
        select(models.Book)
    )
    return result.scalars().all()


async def get_book(db: AsyncSession, book_id):
    result = await db.execute(
        select(Book).where(Book.id == book_id)
        )
    return result.scalar_one_or_none()


async def update_book(db: AsyncSession, book_id: int, updated_book: schemas.BookCreate):
    result = await db.execute(
        select(models.Book).where(models.Book.id == book_id)
    )

    book = result.scalar_one_or_none()

    if not book:
        return None

    book.title = updated_book.title
    book.author = updated_book.author

    await db.commit()
    await db.refresh(book)

    return book


async def delete_book(db: AsyncSession, book_id: int):
    result = await db.execute(
        select(models.Book).where(models.Book.id == book_id)
    )

    book = result.scalar_one_or_none()

    if not book:
        return None

    await db.delete(book)
    await db.commit()

    return "This book is deleted"


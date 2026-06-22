from app import crud
from app.dependency import get_db
from app.schemas import BookCreate
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", status_code=200)
async def get_books(db: AsyncSession = Depends(get_db)):
    return await crud.get_books(db)


@router.get("/{book_id}", status_code=200)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_book(db, book_id)


@router.post("/", status_code=201)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_book(db, book)


@router.put("/{book_id}")
async def update_book(book_id: int, book: BookCreate, db: AsyncSession = Depends(get_db)):
    updated = await crud.update_book(db, book_id, book)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return updated


@router.delete("/{book_id}", status_code=204)
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.delete_book(db, book_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return None

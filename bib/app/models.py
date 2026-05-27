from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book():
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True) # mapped_column нужен для описания колонки в базе данных
    autor: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    
    
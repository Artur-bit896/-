from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Book(Base):
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(
        primary_key=True
    )  # mapped_column нужен для описания колонки в базе данных
    author: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()

from app.database import Base, engine
from app.router import books
from fastapi import FastAPI

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(books.router)

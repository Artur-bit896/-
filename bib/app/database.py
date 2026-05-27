from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./finance.db"


engine = create_engine(DATABASE_URL) # нужен для подключения к базе данных

SessionLocal = sessionmaker(bind=engine) # это нужно для обработки запросов

Base = declarative_base() # нужно для того чтобы для модели было место в таблице

SessionLocal = sessionmaker(bind=engine) # нужен для создания Session — объектов

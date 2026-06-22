from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = (
    "postgresql+psycopg://postgres:090909artur@localhost:5432/finance"
)

engine = create_async_engine(
    DATABASE_URL,
    ehco = True)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession, # значит сделай не обычные session а асинхронные
    expire_on_commit=False,
)


Base = declarative_base()

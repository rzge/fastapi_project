from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings
DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_NAME = "postgres"

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{settings.DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_PARAMS = {}
if settings.MODE == "TEST":
    DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{settings.DB_PASS}@{DB_HOST}:{DB_PORT}/test_booking_db"
    DATABASE_PARAMS = {"poolclass": NullPool}

engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):  # используется для миграций
    pass

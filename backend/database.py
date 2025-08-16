from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

# The connect_args is specific to SQLite to allow multi-threaded access.
engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# The async_sessionmaker provides a factory for creating new async sessions.
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our declarative models.
Base = declarative_base()

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
import sys

# Add the parent directory to the path to allow imports from the 'backend' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from database import Base
# Import the get_db dependency from the routers to override it
from routers.templates import get_db as templates_get_db
from routers.content import get_db as content_get_db

# Use a separate SQLite database for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_blog.db"

engine = create_async_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def override_get_db():
    """
    Dependency override that provides a session to the test database.
    """
    async with TestingSessionLocal() as session:
        yield session

# Override the get_db dependency in the main app for both routers
app.dependency_overrides[templates_get_db] = override_get_db
app.dependency_overrides[content_get_db] = override_get_db


@pytest.fixture(scope="function")
async def client():
    """
    An asynchronous test client fixture that handles the database lifecycle.
    It creates the database tables before each test and drops them afterwards.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    # Clean up the test database file after the test runs
    if os.path.exists("./test_blog.db"):
        os.remove("./test_blog.db")

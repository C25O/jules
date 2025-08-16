from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routers import templates, content

app = FastAPI(title="Markdown-Based Blog Management System")

# Include the API routers
app.include_router(templates.router, prefix="/api/v1", tags=["Templates"])
app.include_router(content.router, prefix="/api/v1", tags=["Content"])


@app.on_event("startup")
async def startup():
    """
    This function runs on application startup and creates the database tables.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint for the API.
    """
    return {"message": "Welcome to the Blog Management System API"}

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .. import crud, schemas, services
from ..database import SessionLocal

router = APIRouter()

# Dependency to get a DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/content/", response_model=schemas.ContentItem)
async def create_content_item(item: schemas.ContentItemCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new content item based on a template.
    """
    # Check if the template exists
    template = await crud.get_template(db, item.template_id)
    if not template:
        raise HTTPException(status_code=404, detail=f"Template with id {item.template_id} not found")

    # Basic validation: Check if the number of values matches the number of fields
    if len(item.values) != len(template.fields):
        raise HTTPException(status_code=400, detail="Number of values does not match number of template fields")

    # More advanced validation (optional for now, but good to have):
    # - Check if all required fields are present
    # - Check if field_ids in values are valid for this template

    return await crud.create_content_item(db=db, item=item)

@router.get("/content/", response_model=List[schemas.ContentItem])
async def read_content_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """
    Retrieve all content items.
    """
    items = await crud.get_content_items(db, skip=skip, limit=limit)
    return items

@router.get("/content/{item_id}", response_model=schemas.ContentItem)
async def read_content_item(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a single content item by its ID.
    """
    db_item = await crud.get_content_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Content item not found")
    return db_item

@router.get("/content/{item_id}/markdown", response_class=PlainTextResponse)
async def get_content_item_as_markdown(item_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a single content item formatted as a Markdown file.
    """
    # Use the specialized crud function to ensure all data is loaded efficiently
    db_item = await crud.get_content_item_for_markdown(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Content item not found")

    markdown_content = services.generate_markdown_from_item(db_item)
    return markdown_content

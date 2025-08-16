from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from .. import crud, schemas
from ..database import SessionLocal, engine
from ..models import Base

router = APIRouter()

# Dependency to get a DB session
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/templates/", response_model=schemas.PageTemplate)
async def create_template(template: schemas.PageTemplateCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new page template.
    """
    db_template = await crud.get_template_by_name(db, name=template.name)
    if db_template:
        raise HTTPException(status_code=400, detail="Template with this name already exists")
    return await crud.create_template(db=db, template=template)

@router.get("/templates/", response_model=List[schemas.PageTemplate])
async def read_templates(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """
    Retrieve all page templates.
    """
    templates = await crud.get_templates(db, skip=skip, limit=limit)
    return templates

@router.get("/templates/{template_id}", response_model=schemas.PageTemplate)
async def read_template(template_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve a single page template by its ID.
    """
    db_template = await crud.get_template(db, template_id=template_id)
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return db_template

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload, joinedload

import models, schemas


# --- Template CRUD Operations ---

async def get_template(db: AsyncSession, template_id: int):
    """
    Retrieves a single page template by its ID, including its associated fields.
    """
    query = select(models.PageTemplate).filter(models.PageTemplate.id == template_id).options(selectinload(models.PageTemplate.fields))
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_template_by_name(db: AsyncSession, name: str):
    """
    Retrieves a single page template by its name.
    """
    query = select(models.PageTemplate).filter(models.PageTemplate.name == name)
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_templates(db: AsyncSession, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of page templates.
    """
    query = select(models.PageTemplate).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def create_template(db: AsyncSession, template: schemas.PageTemplateCreate):
    """
    Creates a new page template and its associated fields.
    """
    # Create the template instance
    db_template = models.PageTemplate(name=template.name, description=template.description)
    db.add(db_template)

    # We need to commit here to get the db_template.id for the fields
    await db.commit()
    await db.refresh(db_template)

    # Create and add the field instances
    for field_data in template.fields:
        db_field = models.TemplateField(**field_data.model_dump(), template_id=db_template.id)
        db.add(db_field)

    # Commit the fields
    await db.commit()
    await db.refresh(db_template)
    return db_template


# --- Content CRUD Operations ---

async def get_content_item(db: AsyncSession, item_id: int):
    """
    Retrieves a single content item by its ID, including its values.
    """
    query = select(models.ContentItem).filter(models.ContentItem.id == item_id).options(selectinload(models.ContentItem.values))
    result = await db.execute(query)
    return result.scalar_one_or_none()

async def get_content_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    """
    Retrieves a list of content items.
    """
    query = select(models.ContentItem).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()

async def create_content_item(db: AsyncSession, item: schemas.ContentItemCreate):
    """
    Creates a new content item and its associated values.
    """
    db_item = models.ContentItem(title=item.title, template_id=item.template_id)
    db.add(db_item)

    # Commit to get the db_item.id
    await db.commit()
    await db.refresh(db_item)

    # Create and add the content values
    for value_data in item.values:
        db_value = models.ContentValue(**value_data.model_dump(), item_id=db_item.id)
        db.add(db_value)

    await db.commit()
    await db.refresh(db_item)
    return db_item

async def get_content_item_for_markdown(db: AsyncSession, item_id: int):
    """
    Retrieves a content item with all necessary relationships eagerly loaded for markdown generation.
    """
    query = (
        select(models.ContentItem)
        .filter(models.ContentItem.id == item_id)
        .options(
            selectinload(models.ContentItem.values).joinedload(models.ContentValue.field)
        )
    )
    result = await db.execute(query)
    return result.scalar_one_or_none()

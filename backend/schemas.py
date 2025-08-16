from pydantic import BaseModel
from typing import List, Optional, Any
import datetime

# Schemas for TemplateField
class TemplateFieldBase(BaseModel):
    name: str
    data_type: str
    required: bool = True

class TemplateFieldCreate(TemplateFieldBase):
    pass

class TemplateField(TemplateFieldBase):
    id: int

    class Config:
        from_attributes = True

# Schemas for PageTemplate
class PageTemplateBase(BaseModel):
    name: str
    description: Optional[str] = None

class PageTemplateCreate(PageTemplateBase):
    fields: List[TemplateFieldCreate]

class PageTemplate(PageTemplateBase):
    id: int
    fields: List[TemplateField] = []

    class Config:
        from_attributes = True

# Schemas for ContentValue
class ContentValueBase(BaseModel):
    field_id: int
    value: Any

class ContentValueCreate(ContentValueBase):
    pass

class ContentValue(ContentValueBase):
    id: int

    class Config:
        from_attributes = True

# Schemas for ContentItem
class ContentItemBase(BaseModel):
    title: str
    template_id: int

class ContentItemCreate(ContentItemBase):
    values: List[ContentValueCreate]

class ContentItem(ContentItemBase):
    id: int
    created_at: datetime.datetime
    values: List[ContentValue] = []

    class Config:
        from_attributes = True

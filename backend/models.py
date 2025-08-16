import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class PageTemplate(Base):
    __tablename__ = "page_templates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String)

    fields = relationship("TemplateField", back_populates="template", cascade="all, delete-orphan")

class TemplateField(Base):
    __tablename__ = "template_fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    data_type = Column(String, nullable=False)
    required = Column(Boolean, default=True)
    template_id = Column(Integer, ForeignKey("page_templates.id"), nullable=False)

    template = relationship("PageTemplate", back_populates="fields")

class ContentItem(Base):
    __tablename__ = "content_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    template_id = Column(Integer, ForeignKey("page_templates.id"), nullable=False)

    template = relationship("PageTemplate")
    values = relationship("ContentValue", back_populates="item", cascade="all, delete-orphan")

class ContentValue(Base):
    __tablename__ = "content_values"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("content_items.id"), nullable=False)
    field_id = Column(Integer, ForeignKey("template_fields.id"), nullable=False)

    value = Column(JSON)

    item = relationship("ContentItem", back_populates="values")
    field = relationship("TemplateField")

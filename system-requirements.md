# Markdown-Based Blog Management System - Development Prompt

## Project Overview
Build a flexible, user-friendly blog management system that allows users to create custom page templates and data types, with all content ultimately stored and exported as Markdown files. The system should provide a visual interface for template creation and content management while maintaining the simplicity and portability of Markdown.

## Core Requirements

### 1. Custom Page Templates

#### Template Creation & Management
- **Visual Template Builder**: Implement a drag-and-drop or form-based interface for creating templates
- **Template Components**: Support for headers, content blocks, sidebars, metadata sections
- **Template Inheritance**: Allow templates to extend from base templates
- **Template Versioning**: Track changes to templates with version history
- **Template Library**: Pre-built templates for common use cases (blog post, landing page, portfolio, documentation)

#### Template Functionality
- Define layout structure with configurable zones/regions
- Set required vs optional fields for each template
- Specify field validation rules
- Configure default values for fields
- Support for conditional rendering based on field values
- Template preview with sample data

### 2. Custom Data Types

#### Built-in Data Types
Implement the following core data types:
- **Text**: Single line text input
- **Rich Text**: Markdown editor with preview
- **Date/DateTime**: Date picker with formatting options
- **Number**: Integer or decimal with min/max validation
- **Boolean**: Checkbox or toggle
- **Select**: Dropdown with predefined options
- **Multi-select**: Multiple choice selection
- **Tags**: Dynamic tag input with autocomplete
- **URL**: URL validation and formatting
- **Email**: Email validation
- **Image**: Image upload/URL with alt text
- **Gallery**: Multiple images with captions
- **Author**: Reference to author profile
- **Related Posts**: Link to other content
- **Featured Product**: Product reference with metadata
- **Code Block**: Syntax-highlighted code snippets
- **JSON**: Structured data input
- **Location**: Geographic coordinates or address

#### Custom Data Type Creation
- Interface for defining new data types
- Composite types (combining existing types)
- Custom validation rules using regex or functions
- Custom rendering templates for each type
- Import/export data type definitions

### 3. Markdown Mapping & Output

#### Markdown Generation
- **Front Matter**: YAML/TOML front matter for metadata
- **Content Mapping**: Clear rules for how each data type converts to Markdown
- **Custom Shortcodes**: Support for custom Markdown extensions (e.g., `{{gallery:id}}`)
- **Clean Output**: Well-formatted, human-readable Markdown files
- **Preserve Formatting**: Maintain user's Markdown formatting preferences

#### Example Markdown Output Structure
```markdown
---
title: "Blog Post Title"
date: 2024-01-15
author: "John Doe"
tags: ["technology", "tutorial"]
featured_image: "/images/hero.jpg"
featured_product: 
  id: "prod-123"
  name: "Product Name"
  price: 99.99
custom_field: "value"
---

# Main Content Here

Blog post content with **markdown** formatting...

{{gallery:summer-photos}}

More content...
```

### 4. User Interface Requirements

#### Content Editor
- Split-pane editor with live Markdown preview
- WYSIWYG mode option with Markdown export
- Field-based form interface based on template
- Drag-and-drop file uploads
- Auto-save functionality
- Revision history with diff viewer

#### Template Designer
- Visual template builder interface
- Field configuration panel
- Live preview with sample data
- Import/export templates as JSON/YAML
- Template testing mode

#### Data Type Manager
- List view of all custom data types
- Create/edit/delete data types
- Field property configuration
- Validation rule builder
- Usage tracking (which templates use which types)

### 5. Technical Specifications

#### Backend Requirements
- **API Design**: RESTful API or GraphQL for all operations
- **Database**: Store templates, data types, and content metadata
- **File System**: Markdown files stored in organized directory structure
- **Validation**: Server-side validation for all data types
- **Export/Import**: Bulk import/export functionality for content and templates

#### Frontend Requirements
- **Framework**: React, Vue, or Angular for dynamic UI
- **State Management**: Proper state management for complex forms
- **Real-time Preview**: Live Markdown rendering
- **Responsive Design**: Mobile-friendly interface
- **Accessibility**: WCAG 2.1 AA compliance

#### Storage & Performance
- **Version Control**: Git integration for tracking changes
- **Caching**: Template and content caching for performance
- **Search**: Full-text search across all content
- **Batch Operations**: Bulk edit/delete/export capabilities

### 6. Additional Features

#### Content Management
- **Categories & Taxonomies**: Organize content hierarchically
- **Draft/Published States**: Content workflow management
- **Scheduling**: Future-dated publishing
- **Multi-language Support**: i18n for content and UI

#### Integration & Extensions
- **Plugin System**: Extensible architecture for custom functionality
- **Webhook Support**: Trigger external services on events
- **API Access**: Public API for headless CMS usage
- **Static Site Generator Integration**: Export for Jekyll, Hugo, Gatsby, etc.

#### Security & Permissions
- **User Roles**: Admin, Editor, Author, Viewer
- **Field-level Permissions**: Control who can edit specific fields
- **API Authentication**: JWT or OAuth2
- **Input Sanitization**: Prevent XSS and injection attacks

## Deliverables

1. **Source Code**: Well-documented, modular codebase
2. **Database Schema**: Normalized database design
3. **API Documentation**: Complete API reference with examples
4. **User Documentation**: End-user guide for template creation and content management
5. **Developer Documentation**: Setup, configuration, and extension guides
6. **Test Suite**: Unit and integration tests with >80% coverage
7. **Deployment Guide**: Instructions for production deployment
8. **Sample Templates**: 5-10 pre-built templates for common use cases

## Success Criteria

- Users can create custom templates without coding
- All content is stored as valid, portable Markdown
- System handles 10,000+ posts efficiently
- Template changes don't break existing content
- Clean separation between content and presentation
- Export functionality works with major static site generators
- Intuitive UI that non-technical users can navigate

## Technical Constraints

- Must generate standard Markdown files compatible with CommonMark
- Front matter should use YAML format by default
- System should work with existing Markdown files (import capability)
- API should follow REST or GraphQL best practices
- Must support UTF-8 encoding for international content

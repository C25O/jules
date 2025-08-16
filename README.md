# Markdown-Based Blog Management System

This project is a flexible, user-friendly blog management system that allows users to create custom page templates and data types, with all content ultimately stored and exported as Markdown files. The system provides a visual interface for template creation and content management while maintaining the simplicity and portability of Markdown.

This repository contains the full-stack implementation, including a FastAPI backend and a React frontend.

## Features

### Backend (Phase 1)
- **RESTful API**: A robust API built with FastAPI for managing templates and content.
- **Custom Templates**: Ability to create page templates with custom-defined fields (e.g., text, rich text, boolean).
- **Dynamic Content**: Create content items based on the structure of a chosen template.
- **Markdown Generation**: An endpoint to export any content item as a clean, human-readable Markdown file with YAML front matter.
- **Database**: Uses SQLAlchemy and a SQLite database for data persistence.

### Frontend (Phase 1)
- **React UI**: A modern, responsive single-page application built with React and Vite.
- **Component Library**: Uses Material-UI for a clean and consistent design.
- **Template Management**: A UI for listing all page templates and a dynamic form for creating new ones.
- **Content Management**: A UI for listing all content items and a dynamic, two-step form for creating new content based on a selected template.
- **Navigation**: A clear and consistent layout with sidebar navigation.

## Tech Stack

- **Backend**: Python, FastAPI, SQLAlchemy, Uvicorn
- **Frontend**: JavaScript, React, Vite, Material-UI, Axios
- **Database**: SQLite

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js v16+ and npm

### Backend Setup
1.  Navigate to the backend directory:
    ```sh
    cd backend
    ```
2.  Create and activate a Python virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    # On Windows, use: venv\\Scripts\\activate
    ```
3.  Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4.  Run the backend server:
    ```sh
    uvicorn main:app --reload
    ```
    The backend API will be available at `http://localhost:8000`.

### Frontend Setup
1.  Navigate to the frontend directory in a new terminal:
    ```sh
    cd frontend
    ```
2.  Install the required npm packages:
    ```sh
    npm install
    ```
3.  Run the frontend development server:
    ```sh
    npm run dev
    ```
    The frontend application will be available at `http://localhost:5173` (or another port if 5173 is in use).

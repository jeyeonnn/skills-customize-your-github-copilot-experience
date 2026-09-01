# 📘 Assignment: Building a Student Task Tracker with FastAPI and SQLite

## 🎯 Objective

Build a small backend application that helps students manage their tasks and assignments. You will learn how to create a REST API with FastAPI, validate data with Pydantic, and save information in a SQLite database using Python.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description

Create the foundation for your student task tracker by setting up a FastAPI application and defining the data model for tasks. This task focuses on creating a clean API structure and preparing the project for future features.

#### Requirements

Completed program should:

- Create a FastAPI application using `FastAPI()`
- Define a task model with fields such as `id`, `title`, `description`, `completed`, and `due_date`
- Use Pydantic models to validate task data
- Include at least one root endpoint that returns a welcome message
- Start the app successfully with `uvicorn main:app --reload`

### 🛠️ Implement CRUD Endpoints

#### Description

Add API routes to create, read, update, and delete tasks. This task introduces the main behaviors of a REST API and helps students practice working with JSON data and HTTP methods.

#### Requirements

Completed program should:

- Create a `POST /tasks` endpoint to add a new task
- Create a `GET /tasks` endpoint to list all tasks
- Create a `GET /tasks/{task_id}` endpoint to view one task by ID
- Create a `PUT /tasks/{task_id}` endpoint to update an existing task
- Create a `DELETE /tasks/{task_id}` endpoint to remove a task
- Return helpful responses and correct HTTP status codes
- Validate task data before saving or updating it

### 🛠️ Store Data in SQLite

#### Description

Move the application from in-memory storage to a SQLite database so tasks remain saved between requests. This task teaches students how real applications persist data and how backend services interact with databases.

#### Requirements

Completed program should:

- Connect to a SQLite database using Python's built-in `sqlite3` module or SQLAlchemy
- Create a `tasks` table with appropriate columns
- Save new task data in the database instead of only keeping it in memory
- Query tasks from the database in list and detail endpoints
- Update and delete task records in the database
- Return meaningful error messages when a task cannot be found

#### Example

```json
{
  "id": 1,
  "title": "Finish Python homework",
  "description": "Complete the functions exercise before Friday.",
  "completed": false,
  "due_date": "2026-09-10"
}
```

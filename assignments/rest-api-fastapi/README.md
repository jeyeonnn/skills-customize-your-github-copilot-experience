# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and performant REST APIs using the FastAPI framework. You will create a complete API with multiple endpoints, data validation, and error handling, gaining experience with modern Python web development patterns.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description

Set up a new FastAPI application and create your first endpoint. You'll build the foundation for a simple TODO item API with proper project structure and dependencies.

#### Requirements

Completed program should:

- Import and initialize FastAPI with `FastAPI()` 
- Create at least one GET endpoint that returns a welcome message or simple data
- Define a Pydantic model for data structure (e.g., Todo with fields for id, title, description, completed status)
- Include proper docstrings and type hints for all functions
- Run successfully when started with `uvicorn main:app --reload`

#### Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False

@app.get("/")
def read_root():
    return {"message": "Welcome to the TODO API"}
```

### 🛠️ Implement CRUD Endpoints

#### Description

Extend your API to support full CRUD operations (Create, Read, Update, Delete) for TODO items. You'll work with request bodies, path parameters, and in-memory data storage.

#### Requirements

Completed program should:

- Implement a POST endpoint to create new TODO items and return the created item
- Implement a GET endpoint to retrieve a specific TODO item by ID
- Implement a GET endpoint to retrieve all TODO items
- Implement a PUT endpoint to update an existing TODO item
- Implement a DELETE endpoint to remove a TODO item by ID
- Store TODO items in a list or dictionary during runtime
- Return appropriate HTTP status codes (201 for creation, 200 for success, 404 for not found)

#### Example

```
POST /todos → Create a new TODO
GET /todos → List all TODOs
GET /todos/{id} → Get a specific TODO
PUT /todos/{id} → Update a TODO
DELETE /todos/{id} → Delete a TODO
```

### 🛠️ Add Data Validation and Error Handling

#### Description

Improve your API's robustness by adding comprehensive data validation and error handling. Handle edge cases and provide meaningful error messages to API clients.

#### Requirements

Completed program should:

- Use Pydantic models to validate request data (required fields, type checking, etc.)
- Return 400 Bad Request for invalid input data
- Return 404 Not Found when requesting a TODO that doesn't exist
- Return 409 Conflict or appropriate status for duplicate or invalid operations
- Provide clear error messages in JSON format
- Use FastAPI's HTTPException for error responses
- Include input validation such as non-empty titles and valid status values

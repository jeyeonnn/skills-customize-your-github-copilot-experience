from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize the FastAPI application
app = FastAPI(title="TODO API", version="1.0.0")

# Pydantic model for TODO items
class Todo(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for TODO items
todos: List[Todo] = []
next_id = 1

# TODO: Implement the following endpoints:
# 1. GET / - Welcome message
# 2. POST /todos - Create a new TODO
# 3. GET /todos - List all TODOs
# 4. GET /todos/{id} - Get a specific TODO
# 5. PUT /todos/{id} - Update a TODO
# 6. DELETE /todos/{id} - Delete a TODO

# Example endpoint (delete this when implementing):
@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the TODO API"}

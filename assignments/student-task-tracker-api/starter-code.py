from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import sqlite3

app = FastAPI(title="Student Task Tracker API")


class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[str] = None


# TODO: Create a database connection and initialize the tasks table
# TODO: Implement GET /
# TODO: Implement POST /tasks
# TODO: Implement GET /tasks
# TODO: Implement GET /tasks/{task_id}
# TODO: Implement PUT /tasks/{task_id}
# TODO: Implement DELETE /tasks/{task_id}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Task Tracker API"}

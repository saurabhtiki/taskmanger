from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100) # ... means required
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass # Inherits fields from TaskBase

class TaskUpdate(TaskBase):
    # For updates, all fields can be optional
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskInDB(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True # Essential for SQLAlchemy ORM compatibility
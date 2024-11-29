from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models import Task
from app.schemas import TaskSchema, TaskResponse
from typing import List

router = APIRouter()

# Create a task
@router.post("/", response_model=TaskResponse)
async def create_task(task: TaskSchema, db: AsyncSession = Depends(get_db)):
    try:
        new_task = Task(title=task.title, completed=task.completed)
        db.add(new_task)
        await db.commit()  # Ensure this happens
        await db.refresh(new_task)
        return new_task
    except Exception as e:
        print(f"Error during task creation: {e}")
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


# Get all tasks
@router.get("/", response_model=List[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks

# Get one task
@router.get("task-details/{id}", response_model=TaskResponse)
async def get_task(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == id))
    db_item = result.scalar_one_or_none()  # Extract the single result or None
    if db_item is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_item


# Update a task
@router.put("/{id}", response_model=TaskResponse)
async def update_task(id: int, task: TaskSchema, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == id))
    existing_task = result.scalar_one_or_none()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    existing_task.title = task.title
    existing_task.completed = task.completed
    await db.commit()
    await db.refresh(existing_task)
    return existing_task

# Delete a task
@router.delete("/{id}")
async def delete_task(id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == id))
    task = result.scalar_one_or_none()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(task)
    await db.commit()
    return {"status": "deleted"}

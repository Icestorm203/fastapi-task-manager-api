from fastapi import APIRouter
from fastapi import HTTPException

from ..database import SessionLocal
from ..schemas import TaskCreate
from .. import crud

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
def get_tasks():

    db = SessionLocal()

    tasks = crud.get_tasks(db)

    db.close()

    return tasks


@router.post("")
def create_task(task: TaskCreate):

    db = SessionLocal()

    result = crud.create_task(db, task)

    db.close()

    return result


@router.put("/{task_id}")
def close_task(task_id: int):

    db = SessionLocal()

    task = crud.close_task(db, task_id)

    db.close()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task



@router.delete("/{task_id}")
def delete_task(task_id: int):

    db = SessionLocal()

    task = crud.delete_task(db, task_id)

    db.close()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted"
    }
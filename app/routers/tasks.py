from fastapi import APIRouter
from fastapi import HTTPException

from ..database import SessionLocal
from ..schemas import TaskCreate
from .. import crud
from ..auth import get_current_user
from fastapi import Depends

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("")
def get_tasks(current_user = Depends(get_current_user)):

    db = SessionLocal()

    tasks = crud.get_tasks(db, current_user)

    db.close()

    return tasks


@router.post("")
def create_task(task: TaskCreate, current_user = Depends(get_current_user)):

    db = SessionLocal()

    result = crud.create_task(db, task, current_user)

    db.close()

    return result


@router.put("/{task_id}")
def close_task(task_id: int, current_user = Depends(get_current_user)):

    db = SessionLocal()

    task = crud.close_task(db, task_id,current_user)

    db.close()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task



@router.delete("/{task_id}")
def delete_task(task_id: int, current_user = Depends(get_current_user)):

    db = SessionLocal()

    task = crud.delete_task(db, task_id, current_user)

    db.close()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted"
    }
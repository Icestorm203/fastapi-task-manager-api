from .models import Task


def get_tasks(db):

    return db.query(Task).all()


def create_task(db, task_data):

    task = Task(
        title=task_data.title,
        is_closed=False
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def close_task(db, task_id):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if task:

        task.is_closed = True

        db.commit()

        db.refresh(task)

    return task


def delete_task(db, task_id):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if task:

        db.delete(task)

        db.commit()

    return task
from .models import Task


def get_tasks(db, current_user):

    return db.query(Task).filter(Task.user_id == current_user.id).all()


def create_task(db, task_data, current_user):

    task = Task(
        title=task_data.title,
        is_closed=False,
        user_id=current_user.id
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def close_task(db, task_id, current_user):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id
    ).first()

    if task:

        task.is_closed = True

        db.commit()

        db.refresh(task)

    return task


def delete_task(db, task_id, current_user):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id
    ).first()

    if task:

        db.delete(task)

        db.commit()

    return task
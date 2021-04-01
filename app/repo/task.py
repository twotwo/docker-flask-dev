from app.domain import db
from app.domain.task import Task


def get_tasks():
    return Task.query.all()


def create_task(title, text):
    new_task = Task(title=title, text=text)
    db.session.add(new_task)
    db.session.commit()
    return new_task


def done(id):
    task = Task.query.filter_by(id=int(id)).first()
    task.done = not (task.done)
    db.session.commit()


def delete(id):
    Task.query.filter_by(id=int(id)).delete()
    db.session.commit()
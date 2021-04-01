import datetime

from app.domain import ModelMixin, db


class Task(db.Model, ModelMixin):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.String)
    done = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(
        db.DateTime,
        onupdate=datetime.datetime.now,
        default=datetime.datetime.now
    )

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False

    def __repr__(self):
        return f"{self.title} - {self.text}"

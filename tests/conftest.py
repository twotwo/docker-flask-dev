# https://github.com/pallets/flask-sqlalchemy/blob/master/tests/conftest.py

from datetime import datetime

from app import create_app
import os
import pytest

from flask_sqlalchemy import SQLAlchemy


@pytest.fixture
def app(request):
    app = create_app(os.getenv("FLASK_CONFIG", "testing"))
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    _db = SQLAlchemy(app)
    with app.app_context():
        _db.init_app(app)
        _db.create_all()
    return _db


@pytest.fixture
def Todo(db):
    class Todo(db.Model):
        __tablename__ = "todos"
        id = db.Column("todo_id", db.Integer, primary_key=True)
        title = db.Column(db.String(60))
        text = db.Column(db.String)
        done = db.Column(db.Boolean)
        pub_date = db.Column(db.DateTime)

        def __init__(self, title, text):
            self.title = title
            self.text = text
            self.done = False
            self.pub_date = datetime.utcnow()

    db.create_all()
    yield Todo
    db.drop_all()

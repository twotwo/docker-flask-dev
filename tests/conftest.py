# https://github.com/pallets/flask-sqlalchemy/blob/master/tests/conftest.py

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from app import create_app
import os
import pytest

from app.domain import db as _db


@pytest.fixture
def app(request):
    app = create_app(os.getenv("FLASK_CONFIG", "testing"))
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture(autouse=True)
def db(app):
    with app.app_context():
        _db.init_app(app)
        _db.create_all()
    return _db

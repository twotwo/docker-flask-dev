# -*- coding: utf-8 -*-
import os
import tempfile

import pytest

from app import create_app
from app.database import get_database, init_database
from app.setting import sqlite_prefix


@pytest.fixture
def app():
    """
    Create and configure a new app instance for each test.
    """
    # create the app with common test config
    app = create_app(config_name="testing")
    app.config["SECRET_KEY"] = "test key"
    app.config["SQLALCHEMY_ECHO"] = False

    # create a temporary file to isolate the database for each test
    db_fd, db_path = tempfile.mkstemp()
    app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_prefix + db_path

    # ONLY create the database schema
    with app.app_context():
        init_database(drop=True, sql_file=None)
    yield app

    # close and remove the temporary database
    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    """A test client for the app."""
    yield app.test_client()


@pytest.fixture
def runner(app):
    """A test runner for the app's Click commands."""
    yield app.test_cli_runner()


@pytest.fixture
def db(app):
    with app.app_context():
        db = get_database()
        yield db

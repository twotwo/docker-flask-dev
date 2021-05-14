# Flask RESTful with SQLite

See <https://slides.li3huo.com/resource-oriented-design/> for more details.

This branch is a demo project that implements a REST API for a "task app" using:

- Python3
- Flask 1.1
- Flask-SQLAlchemy 2.5(depend on SQLAlchemy 1.4)

## Local Dev Guide

    python3 -m venv venv
    . ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt && \
        pip install -r requirements-dev.txt

### Run

    . ./venv/bin/activate
    pytest app.py   # flask run

### Run tests

    . ./venv/bin/activate
    export PYTHONPATH=.
    pytest
    pytest --cov=app tests

## Deployment (docker)

    docker-compose build && docker-compose up -d

## Features

[RESTful API - Security](./docs/restful-api-security.md)
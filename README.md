# flask-modern-dev

See <http://wiki.li3huo.com/Docker_Python_Dev>

## Local Dev Guide

    python3 -m venv venv
    . ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt && \
        pip install -r requirements-dev.txt

## Run

    . ./venv/bin/activate
    pytest app.py

## Run tests

    . ./venv/bin/activate
    pytest

# flask-modern-dev
See http://wiki.li3huo.com/Docker_Python_Dev

## Project Overview
- [How to Create a modern flask Project](doc/CREATE-HOWTO.md)

## Local Dev Guide

    python3 -m venv venv
    . ./venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt && \
        pip install -r requirements-dev.txt
    app db upgrade
    app populate-db
    
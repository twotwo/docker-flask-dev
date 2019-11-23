# -*- coding: utf-8 -*-
from flask import current_app

from app.extension import db


def init_database(drop=False, sql_file=None):
    if drop:
        db.drop_all()
    db.create_all()

    if sql_file:
        with current_app.open_resource(sql_file) as f:
            db.executescript(f.read().decode("utf8"))


def get_database():
    return db

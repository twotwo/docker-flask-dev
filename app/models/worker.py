# -*- coding: utf-8 -*-

from app.extension import db, ma
from app.models.mixin import CRUDMixin


class Worker(db.Model, CRUDMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # id = db.Column(db.Integer, primary_key=True)
    gpu = db.Column(db.Integer, unique=True, comment="对应的 GPU ID")
    default_job = db.Column(db.String(30), default="", comment="Default Job Name")


class WorkerSchema(ma.ModelSchema):
    class Meta:
        model = Worker


worker_schema = WorkerSchema()

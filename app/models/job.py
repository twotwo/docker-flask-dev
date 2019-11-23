# -*- coding: utf-8 -*-
from app.extension import db, ma
from app.models.mixin import CRUDMixin
from app.models.predictor import PredictorSchema
from app.models.repacs import RepacsSchema
from app.models.servlet import ServletSchema


class Job(db.Model, CRUDMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    fields = {
        "id": "id",
        "name": "name",
        "task_type": "taskType",
        "repacs": "repacs",
        "predictor": "predictor",
        "servlets": "servlets",
    }

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), default="", comment="Job Name")
    task_type = db.Column(
        db.String(30), default="", comment="预测任务的类型，例如 predict/ct_lung"
    )
    # n-to-1, add foreign key at n side
    repacs_fk = db.Column(db.Integer, db.ForeignKey("repacs.id"), comment="RePACS 外键")
    repacs = db.relationship("RePACS", backref="jobs", lazy=False)
    # n-to-1, add foreign key at n side
    predictor_fk = db.Column(
        db.Integer, db.ForeignKey("predictor.id"), comment="Predictor 外键"
    )
    predictor = db.relationship("Predictor", backref="jobs", lazy=False)
    # 1-to-n, add relationship at 1 side, remember to add foreign key at n side
    servlets = db.relationship("Servlet")


class JobSchema(ma.ModelSchema):
    class Meta:
        model = Job

    # 'repacs','predictor', 'servlets'
    repacs = ma.Nested(RepacsSchema)
    predictor = ma.Nested(PredictorSchema)
    servlets = ma.Nested(ServletSchema, many=True)


job_schema = JobSchema()
job_schemas = JobSchema(many=True)

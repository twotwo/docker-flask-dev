# -*- coding: utf-8 -*-


from app.extension import db, ma
from app.models.mixin import CRUDMixin


class RePACS(db.Model, CRUDMixin):
    __tablename__ = "repacs"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    fields = {"id": "id", "host": "host", "port": "port"}

    # id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(30), comment="Host or IP Address")
    port = db.Column(db.Integer, default=3333, comment="Port")

    def __repr__(self) -> str:
        return (
            f"<RePACS("
            f" id={self.id},"
            f" host={self.host},"
            f" port={self.port}"
            f" )>"
        )


class RepacsSchema(ma.ModelSchema):
    class Meta:
        model = RePACS


repacs_schema = RepacsSchema()

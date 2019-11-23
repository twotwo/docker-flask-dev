from app.extension import db
from app.models.mixin import CRUDMixin


class Host(db.Model, CRUDMixin):

    fields = {"id": "id", "host": "host", "gpus": "gpus"}

    host = db.Column(db.String(30), comment="Host Name or IP Adress")
    gpus = db.Column(
        db.Integer, default=3333, comment="GPU ID split with comma, like 0,1,2,3"
    )

    def __repr__(self) -> str:
        return (
            f"<Host("
            f" id={self.id},"
            f" host={self.host},"
            f" gpus={self.gpus}"
            f" )>"
        )

from app.extension import db, ma
from app.models.mixin import CRUDMixin


class Servlet(db.Model, CRUDMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    service_type = db.Column(db.String(30))
    grpc_host = db.Column(db.String(30), comment="Host or IP Address")
    grpc_port = db.Column(db.Integer, default=3333, comment="Port")
    mandatory = db.Column(
        db.Boolean, default=True, comment="Is this servlet mandatory?"
    )
    # n-to-1, add foreign key at n side
    job_fk = db.Column(db.Integer, db.ForeignKey("job.id"), comment="Job 外键")

    def __repr__(self) -> str:
        return (
            f"<Servlet("
            f" id={self.id},"
            f" name={self.name},"
            f" service_type={self.service_type},"
            f" grpc_host={self.grpc_host},"
            f" grpc_port={self.grpc_port}"
            f" )>"
        )


class ServletSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Servlet


servlet_schema = ServletSchema()

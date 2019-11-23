from app.extension import db, ma
from app.models.mixin import CRUDMixin


class Predictor(db.Model, CRUDMixin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), default="", comment="适配的 servlet 名称，例如 ct1mm")
    version = db.Column(db.String(30), default="", comment="适配的 servlet 版本")
    shared_memory_name = db.Column(
        db.String(30), default="", comment="Shared Memory Name"
    )
    recon = db.Column(db.JSON, default="", comment="生成 VR 图像的像素大小，例如 512")


class PredictorSchema(ma.ModelSchema):
    class Meta:
        model = Predictor


predictor_schema = PredictorSchema()

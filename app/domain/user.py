import datetime

from app.domain import ModelMixin, db


class User(db.Model, ModelMixin):
    """用户表"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)  # 登录名
    password = db.Column(db.String(12), nullable=False)  # 密码
    role = db.Column(db.Integer, unique=False, nullable=False)  # 1:root 2：manager 3：user
    status = db.Column(db.Integer, unique=False, nullable=False, default=1)  # 0:禁用 1:启用
    is_first_login = db.Column(
        db.Integer, unique=False, nullable=False, default=1
    )  # 是否首次登录 0:否 1:是
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(
        db.DateTime, onupdate=datetime.datetime.now, default=datetime.datetime.now
    )

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.role}"

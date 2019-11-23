# -*- coding: utf-8 -*-

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.extension import db
from app.models.mixin import CRUDMixin, SchemaMixin


class Admin(db.Model, UserMixin, CRUDMixin, SchemaMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), default="", comment="管理员登录名")
    password_hash = db.Column(db.String(128), default="", comment="登录密码的哈希值")
    name = db.Column(db.String(30), default="", comment="姓名")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

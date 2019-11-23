# -*- coding: utf-8 -*-
from datetime import datetime

from app.extension import db
from app.models.schema import get_schema_class


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class SchemaMixin(object):
    _schema = None

    @classmethod
    def symbol(cls) -> dict:
        print(f'class={cls.__name__}, fields = {getattr(cls, "fields", {})}')
        return getattr(cls, "fields", {})

    def dump(self) -> dict:
        return self.get_schema().dump(self)

    def dumps(self) -> str:
        return self.get_schema().dumps(self)

    def get_schema(self):
        if self._schema is None:
            self._schema = get_schema_class(self.__class__, self.symbol())()
        return self._schema


class CRUDMixin(object):
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, nullable=False, comment="唯一标识符")

    @classmethod
    def get_by_id(cls, uid):
        if any((isinstance(uid, str) and uid.isdigit(), isinstance(uid, (int, float)))):
            return cls.query.get(int(uid))
        return None

    @classmethod
    def get_by_kw(cls, **kw):
        return cls.query.filter_by(**kw).all()

    @classmethod
    def get_first_by_kw(cls, **kw):
        return cls.query.filter_by(**kw).first()

    @classmethod
    def get_first_or_create(cls, **kw):
        instance = cls.get_first_by_kw(**kw)
        if not instance:
            instance = cls.create(**kw)
            db.session.add(instance)
        return instance

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

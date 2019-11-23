# -*- coding: utf-8 -*-

from marshmallow import post_dump, post_load, pre_load

from app.extension import ma


def get_schema_class(cls, symbol: dict = None):
    class Schema(ma.ModelSchema):
        class Meta:
            model = cls

        @pre_load
        def pre_load_handler(self, data: dict, **kwargs) -> dict:
            if symbol is None:
                return data
            return {
                symbol[key]: value
                for key, value in data.items()
                if key in symbol.keys()
            }

        @post_load
        def post_load_handler(self, data: dict) -> dict:
            if not data:
                return {}
            return cls(**data)

        @post_dump(pass_many=True)
        def post_dump_handler(self, data: dict, many: bool, **kwargs) -> dict:
            if symbol is None:
                return data
            return {
                symbol[key]: value
                for key, value in data.items()
                if key in symbol.keys()
            }

    return Schema

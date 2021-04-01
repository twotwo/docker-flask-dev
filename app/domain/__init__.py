import json
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION = ["raw_meta", "tags"]
ATTR_NAMES_FOR_APPEND_WRITE = ["product"]


class ModelMixin(object):
    def to_dict(self):
        rt = {}
        if hasattr(self, "__table__"):
            for c in self.__table__.columns:
                value = getattr(self, c.name)
                if type(value) == datetime:
                    value = value.strftime("%Y-%m-%d %H:%M:%S")
                elif c.name in ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION:
                    value = json.loads(value)
                else:
                    pass
                rt[c.name] = value
        return rt

    def copy_from_dict(self, d):
        if hasattr(self, "__table__"):
            for c in self.__table__.columns:
                value = d.get(c.name)
                if value is not None:
                    if c.name in ATTR_NAMES_FOR_JSON_FORMAT_CONVERSION:
                        value = json.dumps(value)
                    elif c.name in ATTR_NAMES_FOR_APPEND_WRITE:
                        origin_value = getattr(self, c.name)
                        if origin_value:
                            if value not in origin_value:
                                origin_value.append(value)
                            value = origin_value
                        else:
                            value = [value]
                    setattr(self, c.name, value)

    def __repr__(self):
        return repr(self.to_dict())

# -*- coding: utf-8 -*-

from flasgger import Swagger
from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
swagger = Swagger()
# https://medium.com/@erdoganyesil/typeerror-object-of-type-is-not-json-serializable-6230ccc74975
ma = Marshmallow()

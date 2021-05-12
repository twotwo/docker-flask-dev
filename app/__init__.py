from flask import Flask

from app.config import config
from app.domain import db


def create_app(config_name):
    _app = Flask(__name__, template_folder=".")
    _app.config.from_object(config[config_name])
    config[config_name].init_app(_app)

    from app.view.index import bp_index

    _app.register_blueprint(bp_index, url_prefix="/")

    from app.view.users import bp_users

    _app.register_blueprint(bp_users, url_prefix="/")


    from app.view.sessions import bp_sessions

    _app.register_blueprint(bp_sessions, url_prefix="/")

    from app.view.api import bp_api

    _app.register_blueprint(bp_api, url_prefix="/api")

    with _app.app_context():
        db.init_app(_app)
        db.create_all()
    return _app


app = create_app("default")


if __name__ == "__main__":
    app.run()

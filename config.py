# https://github.com/miguelgrinberg/flasky/blob/master/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # use memory db
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    # "production": ProductionConfig,
    "default": DevelopmentConfig,
}

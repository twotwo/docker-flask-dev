# -*- coding: utf-8 -*-
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

WIN = sys.platform.startswith("win")
if WIN:
    sqlite_prefix = "sqlite:///"
else:
    sqlite_prefix = "sqlite:////"


class BaseConfig(object):
    SECRET_KEY = os.getenv("SECRET_KEY", "dev key")
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SLOW_QUERY_THRESHOLD = 1
    REPACS_DEFAULT_PAGE = 1
    REPACS_DEFAULT_PER_PAGE = 20
    REPACS_DEFAULT_MAX_PER_PAGE = 100

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.getenv("MYSQL_PORT", 3307)
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "redb")
    MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", "pacs")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "pacs")
    MYSQL_CHARSET = os.getenv("MYSQL_CHARSET", "utf8mb4")
    # 'mysql+pymysql://root:test@localhost/REPACS?charset=utf8mb4'
    MYSQL_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset={charset}".format(
        username=MYSQL_USERNAME,
        password=MYSQL_PASSWORD,
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        database=MYSQL_DATABASE,
        charset=MYSQL_CHARSET,
    )


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_BACKTRACE = True
    LOG_LEVEL = "DEBUG"
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', BaseConfig.MYSQL_URI)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DEV_DATABASE_URL", sqlite_prefix + os.path.join(basedir, "data.db")
    )


class TestingConfig(BaseConfig):
    TESTING = True
    LOG_FILE = os.getenv("LOG_FILE", "")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URL", sqlite_prefix + os.path.join(basedir, "data.db")
    )


class ProductionConfig(BaseConfig):
    LOG_BACKTRACE = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", BaseConfig.MYSQL_URI)


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

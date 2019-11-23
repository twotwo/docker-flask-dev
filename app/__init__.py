# -*- coding: utf-8 -*-
import logging
import logging.handlers
import os
from logging.handlers import RotatingFileHandler

import click
from flask import Flask
from flask_sqlalchemy import get_debug_queries

from app.blueprints.config import config_bp
from app.extension import db, ma, migrate, swagger, toolbar
from app.setting import config

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def create_app(config_name=None):
    """create flask app
    """
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_errors(app)
    register_shell_context(app)
    register_request_handlers(app)

    @app.route("/hello")
    def hello():
        return "Hello, World >W<"

    return app


def register_logging(app):
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_name = app.config.get("LOG_FILE", "logs/app.log")
    if file_name:
        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))

        file_handler = RotatingFileHandler(
            file_name, maxBytes=10 * 1024 * 1024, backupCount=10
        )
        file_handler.setFormatter(formatter)
        file_handler.setLevel(app.config.get("LOG_LEVEL", logging.DEBUG))

        logging.getLogger("werkzeug").setLevel(logging.DEBUG)
        logging.getLogger("werkzeug").addHandler(file_handler)

        app.logger.addHandler(file_handler)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)
    swagger.init_app(app)
    ma.init_app(app)


def register_blueprints(app):
    app.register_blueprint(config_bp, url_prefix="/")


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        # return dict(db=db, Admin=Admin, Post=Post, Category=Category, Comment=Comment)
        return dict()


def register_commands(app):
    @app.cli.command()
    @click.option("--drop", is_flag=True, help="Create after drop.")
    def initdb(drop):
        if drop:
            click.confirm(
                "This operation will delete the database, do you want to continue?",
                abort=True,
            )
            db.drop_all()
            click.echo("Drop tables.")
        db.create_all()
        click.echo("Initialized database.")

    @app.cli.command()
    @click.option("--count", default=4, help="GPU count, default is 4.")
    def forge(count):
        """Generate fake data."""
        from app.commands import forge_cmd

        forge_cmd(db, count)
        click.echo("Done.")


def register_request_handlers(app):
    @app.after_request
    def query_profiler(response):
        for q in get_debug_queries():
            if q.duration >= app.config["SLOW_QUERY_THRESHOLD"]:
                app.logger.warning(
                    "Slow query: Duration: %fs\n Context: %s\nQuery: %s\n "
                    % (q.duration, q.context, q.statement)
                )
        return response


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        app.logger.warning("Bad Request:")
        app.logger.warning(">>>>>>>>>>>>>>>>>")
        app.logger.warning(e)
        app.logger.warning("<<<<<<<<<<<<<<<<<")
        return "Bad Request", 400

    @app.errorhandler(404)
    def page_not_found(e):
        app.logger.warning("Page Not Found:")
        app.logger.warning(">>>>>>>>>>>>>>>>>")
        app.logger.warning(e)
        app.logger.warning("<<<<<<<<<<<<<<<<<")
        return "Page Not Found", 404

    @app.errorhandler(500)
    def internal_server_error(e):
        app.logger.exception("Internal Server Error:")
        app.logger.exception(">>>>>>>>>>>>>>>>>")
        app.logger.exception(e)
        app.logger.exception("<<<<<<<<<<<<<<<<<")
        return "Internal Server Error", 500

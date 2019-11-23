# -*- coding: utf-8 -*-

from flask import Blueprint, render_template

# from flask_login import current_user
from app.services import ConfigInfo, JobHandler

config_bp = Blueprint("config", __name__)


@config_bp.route("/", methods=["GET"])
def index():

    jobs = JobHandler.get_all()
    return render_template("config/index.html", jobs=jobs, config=ConfigInfo.get_all())


@config_bp.route("/about")
def about():
    return render_template("config/about.html")

from flask import Blueprint, abort, jsonify, request

from app.repo import task


bp_api = Blueprint(__name__, __name__)


@bp_api.route("/task", methods=["POST"])
@bp_api.route("/task/", methods=["POST"])
def create_task():
    if request.json is None:
        abort(401)

    title = request.json.get("title")
    text= request.json.get("text")
    return jsonify(task.create_task(title, text).to_dict())


@bp_api.route("/task", methods=["GET"])
@bp_api.route("/task/", methods=["GET"])
def get_tasks():
    return jsonify(task.get_tasks())
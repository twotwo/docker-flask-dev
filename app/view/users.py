from flask import Blueprint, abort, jsonify, request

from app.repo import user


bp_users = Blueprint(__name__, __name__)


@bp_users.route("/users", methods=["GET"])
@bp_users.route("/users/", methods=["GET"])
def get_users():
    users = user.get_users()
    return jsonify([{"id": user.id, "name": user.name} for user in users])


@bp_users.route("/users", methods=["POST"])
@bp_users.route("/users/", methods=["POST"])
def create_user():
    if request.json is None:
        abort(401)

    name = request.json.get("name")
    password = request.json.get("password")
    user_role = request.args.get("user_role", 1, type=int)
    return jsonify(user.create_user(name, password, user_role).to_dict())


@bp_users.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({"id": 11, "name": "user.name"})


@bp_users.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    return jsonify({"id": 11, "name": "user.name"})


@bp_users.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return jsonify({"id": 11, "name": "user.name"})
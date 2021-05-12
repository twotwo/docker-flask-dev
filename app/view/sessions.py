from flask import Blueprint, abort, jsonify, request

from app.repo import user

bp_sessions = Blueprint(__name__, __name__)


@bp_sessions.route("/sessions/<session_id>", methods=["GET"])
def get_session(session_id):
    return f"get session<{session_id}> info from redis"


@bp_sessions.route("/sessions", methods=["POST"])
@bp_sessions.route("/sessions/", methods=["POST"])
def create_session():
    """Login"""
    if request.json is None:
        abort(401)

    name = request.json.get("name")
    password = request.json.get("password")
    user_role = request.args.get("user_role", 1, type=int)
    # check user is valid
    return jsonify("token")

@bp_sessions.route("/sessions/<session_id>", methods=["DELETE"])
def delete_session(session_id):
    """Logout"""
    return f"delete session<{session_id}> info from redis"
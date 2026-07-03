from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/status")
def api_status():

    return jsonify(
        {
            "application": "APTP",
            "status": "online",
            "version": "0.1.0-dev",
        }
    )
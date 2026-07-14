from flask import Blueprint, render_template, request, jsonify

from backend.controllers.metrics_controller import MetricsController

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics")
def metrics():

    return render_template(
        "metrics.html",
        current_page=request.path,
        **MetricsController.get_page_data()
    )

@metrics_bp.route(
    "/metrics/save",
    methods=["POST"]
)
def save():
    MetricsController.save(
        request.get_json()
    )
    return jsonify(success=True)
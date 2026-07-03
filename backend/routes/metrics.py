from flask import Blueprint, render_template, request

from backend.controllers.metrics_controller import MetricsController

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics")
def metrics():

    return render_template(
        "metrics.html",
        current_page=request.path,
        **MetricsController.get_page_data()
    )
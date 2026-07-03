from flask import Blueprint, render_template, request

from backend.controllers.dashboard_controller import DashboardController

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        current_page=request.path,
        **DashboardController.get_page_data()
    )
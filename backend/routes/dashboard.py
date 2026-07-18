from flask import Blueprint, render_template, request, jsonify

from backend.controllers.dashboard_controller import DashboardController

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():

    return render_template(
        "dashboard.html",
        current_page=request.path,
        **DashboardController.get_page_data()
    )

@dashboard_bp.route(

    "/dashboard/wifi-connectivity",

    methods=["GET"]

)
def wifi_connectivity():

    return jsonify(

        DashboardController.get_wifi_connectivity()

    )

@dashboard_bp.route(

    "/dashboard/wifi-signal",

    methods=["GET"]

)
def wifi_signal():

    return jsonify(

        DashboardController.get_wifi_signal()

    )
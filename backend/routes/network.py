from flask import Blueprint, render_template, request, redirect

from backend.controllers.network_controller import NetworkController

network_bp = Blueprint("network", __name__)

@network_bp.route("/network")
def network():

    return render_template(

        "network.html",

        current_page=request.path,

        **NetworkController.get_page_data()

    )

@network_bp.route(
    "/network/scan",
    methods=["POST"]
)
def scan_network():

    NetworkController.scan()

    return ("", 204)

@network_bp.route(
    "/network/clear",
    methods=["POST"]
)
def clear_network():

    NetworkController.clear()

    return ("", 204)

@network_bp.route(
    "/network/connect",
    methods=["POST"]
)
def connect_network():

    return NetworkController.connect()
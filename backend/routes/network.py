from flask import Blueprint, render_template, request

network_bp = Blueprint("network", __name__)

@network_bp.route("/network")
def network():

    return render_template(

        "network.html",

        current_page=request.path

    )
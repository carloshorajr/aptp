from flask import Blueprint, render_template, request

from backend.controllers.system_controller import SystemController

system_bp = Blueprint("system", __name__)

@system_bp.route("/system")
def system():

    return render_template(
        "system.html",
        current_page=request.path,
        **SystemController.get_page_data()
    )
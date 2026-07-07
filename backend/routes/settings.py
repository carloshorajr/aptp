from flask import Blueprint, render_template, request, redirect, flash

from backend.controllers.settings_controller import SettingsController

settings_bp = Blueprint("settings", __name__)

@settings_bp.route("/settings", methods=["GET", "POST"])
def settings():

    if request.method == "POST":
        SettingsController.save(request.form)
        flash("Configurações salvas com sucesso.", "success")
        return redirect("/settings")

    return render_template(
        "settings.html",
        current_page=request.path,
        **SettingsController.get_page_data()
    )

@settings_bp.route("/settings/clear", methods=["POST"])
def clear_settings():

    SettingsController.clear()

    return redirect("/settings")
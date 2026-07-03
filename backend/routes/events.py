from flask import Blueprint, render_template, request, redirect

from backend.controllers.events_controller import EventsController

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def events():

    return render_template(
        "events.html",
        current_page=request.path,
        **EventsController.get_page_data(request.args)
    )

@events_bp.route("/events/clear", methods=["POST"])
def clear_events():

    from backend.services.event_service import EventService

    EventService.clear()

    return redirect("/events")
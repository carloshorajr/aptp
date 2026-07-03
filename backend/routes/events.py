from flask import Blueprint, render_template, request, redirect, jsonify

from backend.controllers.events_controller import EventsController

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def events():

    return render_template(
        "events.html",
        current_page=request.path,
        **EventsController.get_page_data(request.args)
    )

@events_bp.route("/events/data")
def events_data():

    data = EventsController.get_page_data(request.args)

    return jsonify({

        "statistics": data["statistics"],

        "events": [

            {
                "timestamp": event.timestamp.strftime("%d/%m/%y %H:%M"),
                "level": event.level,
                "source": event.source,
                "message": event.message
            }

            for event in data["events"]

        ]

    })

@events_bp.route("/events/clear", methods=["POST"])
def clear_events():

    from backend.services.event_service import EventService

    EventService.clear()

    return redirect("/events")
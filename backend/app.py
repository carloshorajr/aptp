from flask import Flask

from flask import jsonify

import atexit

from backend.routes.dashboard import dashboard_bp
from backend.routes.settings import settings_bp
from backend.routes.metrics import metrics_bp
from backend.routes.events import events_bp
from backend.routes.system import system_bp

from backend.services.runtime_service import RuntimeService

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.secret_key = "sonda-dev"

@app.get("/api/status")
def api_status():

    return jsonify({

        "status": "online",
        "application": "APTP",
        "version": "0.1.0-dev"

    })

app.register_blueprint(dashboard_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(metrics_bp)
app.register_blueprint(events_bp)
app.register_blueprint(system_bp)

RuntimeService.application_started()

atexit.register(
    RuntimeService.application_stopped
)
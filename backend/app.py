from flask import Flask, jsonify

from backend.routes.dashboard import dashboard_bp
from backend.routes.settings import settings_bp
from backend.routes.metrics import metrics_bp
from backend.routes.events import events_bp
from backend.routes.system import system_bp
from backend.routes.api import api_bp

from backend.services.runtime_service import RuntimeService

from backend.core.database_initializer import DatabaseInitializer

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.secret_key = "sonda-dev"

app.register_blueprint(dashboard_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(metrics_bp)
app.register_blueprint(events_bp)
app.register_blueprint(system_bp)
app.register_blueprint(api_bp)

DatabaseInitializer.initialize()

RuntimeService.application_started()
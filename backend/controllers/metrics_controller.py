from backend.services.application_service import (
    ApplicationService
)

from backend.repositories.wifi_metric_settings_repository import (
    WifiMetricSettingsRepository
)


class MetricsController:

    @staticmethod
    def get_page_data():

        settings = WifiMetricSettingsRepository.load("connectivity")

        return {
            "page_title": "Métricas",
            "page_subtitle": "Indicadores coletados",
            "application": ApplicationService.get_application_info(),
            "settings": {
                "connectivity": {
                "enabled": bool(settings["enabled"]),
                "interval_seconds": settings["interval_seconds"]
                }

            }
        }
    
    @staticmethod
    def save(data):

        WifiMetricSettingsRepository.save(
            metric="connectivity",
            enabled=int(data["enabled"]),
            interval_seconds=int(data["interval_seconds"])
        )
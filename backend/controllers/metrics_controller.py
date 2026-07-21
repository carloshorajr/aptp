from backend.services.application_service import (
    ApplicationService
)

from backend.repositories.wifi_metric_settings_repository import (
    WifiMetricSettingsRepository
)

from backend.services.wifi_signal_service import (
    WifiSignalService
)

from backend.services.wifi_connectivity_service import (
    WifiConnectivityService
)


class MetricsController:

    @staticmethod
    def get_page_data():

        connectivity = WifiMetricSettingsRepository.load(
            "connectivity"
        )

        signal = WifiMetricSettingsRepository.load(
            "signal"
        )

        latency = WifiMetricSettingsRepository.load(
            "latency"
        )

        return {
            "page_title": "Métricas",
            "page_subtitle": "Indicadores coletados",
            "application": ApplicationService.get_application_info(),
            "settings": {
                "connectivity": {
                    "enabled": bool(
                        connectivity["enabled"]
                    ),
                    "interval_seconds":
                        connectivity["interval_seconds"]
                },
                "signal": {
                    "enabled": bool(
                        signal["enabled"]
                    ),
                    "interval_seconds":
                        signal["interval_seconds"]
                },
                "latency": {
                    "enabled": bool(
                        latency["enabled"]
                    ),
                    "interval_seconds":
                        latency["interval_seconds"]
                }

            }
        }
    
    @staticmethod
    def save(data):

        WifiMetricSettingsRepository.save(

            metric="connectivity",

            enabled=int(
                data["connectivity"]["enabled"]
            ),

            interval_seconds=int(
                data["connectivity"]["interval_seconds"]
            )

        )

        WifiMetricSettingsRepository.save(

            metric="signal",

            enabled=int(
                data["signal"]["enabled"]
            ),

            interval_seconds=int(
                data["signal"]["interval_seconds"]
            )

        )

        WifiMetricSettingsRepository.save(

            metric="latency",

            enabled=int(

                data["latency"]["enabled"]

            ),

            interval_seconds=int(

                data["latency"]["interval_seconds"]

            )

        )
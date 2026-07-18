from backend.repositories.event_repository import (
    EventRepository
)

from backend.repositories.wifi_metric_settings_repository import (
    WifiMetricSettingsRepository
)

from backend.services.network_service import (
    NetworkService
)

from backend.services.wifi_signal_service import (
    WifiSignalService
)


class DashboardService:

    @staticmethod
    def get_wifi_connectivity():

        settings = WifiMetricSettingsRepository.load(
            "connectivity"
        )

        if not settings["enabled"]:

            return {

                "chart": [],

                "connected_time": None

            }

        return {

            "chart": EventRepository.wifi_connectivity(),

            "connected_time": (
                NetworkService.get_wifi_connected_time()
            )

        }

    @staticmethod
    def get_wifi_signal():

        settings = WifiMetricSettingsRepository.load(
            "signal"
        )

        if not settings["enabled"]:

            return {

                "ssid": None,

                "signal_dbm": None

            }

        wifi = WifiSignalService.current()

        if wifi is None:

            return {

                "ssid": None,

                "signal_dbm": None

            }

        return {

            "ssid": wifi.ssid,

            "signal_dbm": wifi.signal_dbm

        }
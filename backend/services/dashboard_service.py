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

from backend.repositories.wifi_signal_repository import (
    WifiSignalRepository
)


class DashboardService:

    @staticmethod
    def get_widgets():

        return {

            "connectivity":
                WifiMetricSettingsRepository.load(
                    "connectivity"
                )["enabled"],

            "signal":
                WifiMetricSettingsRepository.load(
                    "signal"
                )["enabled"],

            "latency":
                WifiMetricSettingsRepository.load(
                    "latency"
                )["enabled"]

        }

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

                "signal_dbm": None,

                "history": []

            }

        wifi = WifiSignalService.current()

        history = WifiSignalRepository.load_history()

        if wifi is None:

            return {

                "ssid": None,

                "signal_dbm": None,

                "history": history

            }

        return {

            "ssid": wifi.ssid,

            "signal_dbm": wifi.signal_dbm,

            "history": history

        }
    
    @staticmethod
    def get_wifi_latency():

        settings = WifiMetricSettingsRepository.load(
            "latency"
        )

        if not settings["enabled"]:

            return {

                "gateway": None,

                "rtt_avg_ms": None,

                "loss_percent": None

            }

        latency = WifiSignalRepository.load_latency()

        if latency is None:

            return {

                "gateway": None,

                "rtt_avg_ms": None,

                "loss_percent": None

            }

        return latency
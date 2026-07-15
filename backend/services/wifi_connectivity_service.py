from backend.utils.datetime_utils import now

from backend.models.wifi import Wifi

from backend.repositories.wifi_connectivity_repository import (
    WifiConnectivityRepository
)

from backend.repositories.wifi_metric_settings_repository import (
    WifiMetricSettingsRepository
)

from backend.services.wifi_service import (
    WifiService
)

from backend.services.event_service import (
    EventService
)


class WifiConnectivityService:

    _last_execution = None

    @classmethod
    def collect(cls):

        settings = WifiMetricSettingsRepository.load(
            "connectivity"
        )

        if settings is None:

            return None

        if not settings["enabled"]:

            return None

        if (

            settings["interval_seconds"] < 1

            or

            settings["interval_seconds"] > 86400

        ):

            return None

        current = now()

        if cls._last_execution is not None:

            elapsed = (

                current - cls._last_execution

            ).total_seconds()

            if elapsed < settings["interval_seconds"]:

                return None

        cls._last_execution = current

        current = WifiService.collect()

        current.event = None

        previous = WifiConnectivityRepository.load()

        # Primeira execução

        if previous is None:

            current.started_at = (

                current.last_seen

                if current.connected

                else None

            )

            current.connected_time = 0

            WifiConnectivityRepository.save(

                current

            )

            return current

        # Associação
        
        if current.connected:

            if (

                not previous.connected

                or

                previous.ssid != current.ssid

            ):

                current.event = "associated"

                current.started_at = current.last_seen

                current.connected_time = 0

            else:

                current.started_at = previous.started_at

                if previous.started_at is not None:

                    current.connected_time = int(

                        (

                            current.last_seen -

                            previous.started_at

                        ).total_seconds()

                    )

                else:

                    current.connected_time = 0

        # Desassociação

        else:

            if previous.connected:

                current.event = "disassociated"

            current.started_at = None

            current.connected_time = 0
        
        WifiConnectivityRepository.save(current)

        if current.event == "associated":

            EventService.info(

                "WiFi",

                f"Associado à rede WiFi '{current.ssid}'."

            )

        elif current.event == "disassociated":

            EventService.warning(

                "WiFi",

                f"Desassociado da rede WiFi '{previous.ssid}'."

            )
        
        return current
from backend.utils.datetime_utils import now

from backend.repositories.wifi_metric_settings_repository import (
    WifiMetricSettingsRepository
)

from backend.repositories.wifi_signal_repository import (
    WifiSignalRepository
)

from backend.services.wifi_service import (
    WifiService
)

from backend.services.event_service import (
    EventService
)


class WifiSignalService:

    _last_execution = None

    WARNING_DBM = -71

    @classmethod
    def _collect_internal(cls):

        current = WifiService.collect()

        if current.signal_dbm is None:

            return None

        previous = WifiSignalRepository.load()

        #
        # Primeira execução
        #

        if previous is None:

            WifiSignalRepository.save(current)

            return current

        #
        # Nada mudou
        #

        if current.signal_dbm == previous.signal_dbm:

            return current

        #
        # RSSI alterado
        #

        WifiSignalRepository.save(current)

        if current.signal_dbm <= cls.WARNING_DBM:

            EventService.warning(

                "WiFi",

                f"Qualidade do sinal WiFi ruim ({current.signal_dbm} dBm)."

            )

        return current

    @classmethod
    def collect(cls):

        settings = WifiMetricSettingsRepository.load(
            "signal"
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

        return cls._collect_internal()
    
    @classmethod
    def collect_now(cls):

        return cls._collect_internal()
    
    @classmethod
    def current(cls):

        current = WifiService.collect()

        if (

            current.signal_dbm is None

        ):

            return None

        return WifiSignalRepository.load()
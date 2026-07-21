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

    _last_signal_execution = None

    _last_latency_execution = None

    WARNING_DBM = -71

    WARNING_RTT_MS = 10

    ERROR_LOSS_PERCENT = 100

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
    def _collect_latency(cls):

        current = WifiService.collect_latency()

        if current is None:

            return None

        loss_percent = None

        rtt_avg_ms = None

        for line in current["output"].splitlines():

            line = line.strip()

            if "packet loss" in line:

                loss_percent = float(

                    line

                    .split("%")[0]

                    .split()[-1]

                )

            elif line.startswith("rtt "):

                values = (

                    line

                    .split("=")[1]

                    .split()[0]

                    .split("/")

                )

                rtt_avg_ms = float(

                    values[1]

                )

        current["loss_percent"] = loss_percent

        current["rtt_avg_ms"] = rtt_avg_ms

        current["last_seen"] = now()

        previous = WifiSignalRepository.load_latency()

        previous_loss = (

            previous["loss_percent"]

            if previous is not None

            else None

        )

        previous_rtt = (

            previous["rtt_avg_ms"]

            if previous is not None

            else None

        )

        #
        # Primeira execução
        #

        if previous is None:

            WifiSignalRepository.save_latency(

                current

            )

            return current

        #
        # Nada mudou
        #

        if (

            current["loss_percent"] == previous["loss_percent"]

            and

            current["rtt_avg_ms"] == previous["rtt_avg_ms"]

        ):

            return current

        #
        # Latência alterada
        #

        WifiSignalRepository.save_latency(

            current

        )

        #
        # Mudança para perda total
        #

        if (

            current["loss_percent"] == 100

            and

            previous_loss != 100

        ):

            EventService.error(

                "WiFi",

                (

                    "Perda total de comunicação "

                    f"com o gateway {current['gateway']}."

                )

            )

        #
        # Comunicação restabelecida
        #

        elif (

            current["loss_percent"] < 100

            and

            previous_loss == 100

        ):

            EventService.info(

                "WiFi",

                (

                    "Comunicação com o gateway "

                    f"{current['gateway']} restabelecida."

                )

            )

        #
        # Latência elevada
        #

        if (

            current["rtt_avg_ms"] is not None

            and

            current["rtt_avg_ms"] > cls.WARNING_RTT_MS

            and

            (

                previous_rtt is None

                or

                previous_rtt <= cls.WARNING_RTT_MS

            )

        ):

            EventService.warning(

                "WiFi",

                (

                    "Latência elevada com o gateway "

                    f"{current['gateway']} "

                    f"({current['rtt_avg_ms']:.1f} ms)."

                )

            )

        #
        # Latência normalizada
        #

        elif (

            current["rtt_avg_ms"] is not None

            and

            previous_rtt is not None

            and

            current["rtt_avg_ms"] <= cls.WARNING_RTT_MS

            and

            previous_rtt > cls.WARNING_RTT_MS

        ):

            EventService.info(

                "WiFi",

                (

                    "Latência com o gateway "

                    f"{current['gateway']} normalizada "

                    f"({current['rtt_avg_ms']:.1f} ms)."

                )

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

        if cls._last_signal_execution is not None:

            elapsed = (

                current - cls._last_signal_execution

            ).total_seconds()

            if elapsed < settings["interval_seconds"]:

                return None

        cls._last_signal_execution = current

        return cls._collect_internal()

    @classmethod
    def collect_latency(cls):

        settings = WifiMetricSettingsRepository.load(
            "latency"
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

        if cls._last_latency_execution is not None:

            elapsed = (

                current - cls._last_latency_execution

            ).total_seconds()

            if elapsed < settings["interval_seconds"]:

                return None

        cls._last_latency_execution = current

        return cls._collect_latency()
    
    @classmethod
    def collect_now(cls):

        signal = None

        latency = None

        settings = WifiMetricSettingsRepository.load(
            "signal"
        )

        if (

            settings is not None

            and

            settings["enabled"]

        ):

            signal = cls._collect_internal()

        settings = WifiMetricSettingsRepository.load(
            "latency"
        )

        if (

            settings is not None

            and

            settings["enabled"]

        ):

            latency = cls._collect_latency()

        return {

            "signal": signal,

            "latency": latency

        }
    
    @classmethod
    def current(cls):

        current = WifiService.collect()

        if (

            current.signal_dbm is None

        ):

            return None

        return WifiSignalRepository.load()
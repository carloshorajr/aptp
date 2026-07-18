import threading, time

from backend.services.wifi_connectivity_service import (
    WifiConnectivityService
)

from backend.services.wifi_signal_service import (
    WifiSignalService
)


class SchedulerService:

    _thread = None

    _running = False

    @classmethod
    def start(cls):

        if cls._running:

            return

        cls._running = True

        cls._thread = threading.Thread(

            target=cls.run,

            daemon=True

        )

        cls._thread.start()

    @classmethod
    def run(cls):

        while cls._running:

            try:

                WifiConnectivityService.collect()

                WifiSignalService.collect()

            except Exception as e:

                print(e)

            time.sleep(1)
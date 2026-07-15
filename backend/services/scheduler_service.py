import threading, time

from backend.services.wifi_connectivity_service import (
    WifiConnectivityService
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

            except Exception as e:

                print(e)

            time.sleep(1)
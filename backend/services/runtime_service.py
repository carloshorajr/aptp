from backend.repositories.runtime_repository import RuntimeRepository

from backend.services.boot_service import BootService

from backend.services.event_service import EventService

from backend.utils.datetime_utils import now


class RuntimeService:

    @staticmethod
    def application_started():

        runtime = RuntimeRepository.load()

        current_boot = BootService.boot_id()

        current_hostname = BootService.hostname()

        if runtime.get("boot_id") != current_boot:

            EventService.info(

                "Sistema",

                f"{current_hostname} reiniciado."

            )

            runtime["boot_id"] = current_boot

            runtime["hostname"] = current_hostname

            runtime["last_boot"] = now().isoformat()

            RuntimeRepository.save(runtime)
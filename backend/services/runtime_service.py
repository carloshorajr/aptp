from backend.repositories.runtime_repository import RuntimeRepository

from backend.services.event_service import EventService

from backend.utils.datetime_utils import now


class RuntimeService:

    @staticmethod
    def application_started():

        runtime = RuntimeRepository.load()

        if runtime["running"]:

            EventService.warning(
                "Sistema",
                "Inicialização após desligamento inesperado."
            )

        runtime["running"] = True

        runtime["last_start"] = now().isoformat()

        RuntimeRepository.save(runtime)

        EventService.system_started()


    @staticmethod
    def application_stopped():

        runtime = RuntimeRepository.load()

        runtime["running"] = False

        RuntimeRepository.save(runtime)

        EventService.info(
            "Sistema",
            "Sonda encerrada."
        )
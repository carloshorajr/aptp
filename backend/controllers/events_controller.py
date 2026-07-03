from backend.services.event_service import EventService

from backend.services.application_service import ApplicationService

class EventsController:

    @staticmethod
    def get_page_data(filters):

        events = EventService.list(filters)

        events.sort(
            key=lambda e: e.timestamp,
            reverse=True
        )

        return {
            "page_title": "Eventos",
            "page_subtitle": "Registro de ocorrências",
            "events": events,
            "filters": filters,
            "sources": EventService.sources(),
            "statistics": EventService.statistics(),
            "application": ApplicationService.get_application_info()
        }
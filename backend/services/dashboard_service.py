from backend.repositories.event_repository import (
    EventRepository
)


class DashboardService:

    @staticmethod
    def get_wifi_connectivity():

        return EventRepository.wifi_connectivity()
from backend.repositories.event_repository import (
    EventRepository
)

from backend.services.network_service import (
    NetworkService
)

class DashboardService:

    @staticmethod
    def get_wifi_connectivity():

        return {

            "chart": EventRepository.wifi_connectivity(),

            "connected_time": (
                NetworkService.get_wifi_connected_time()
            )

        }
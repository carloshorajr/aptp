from backend.services.system_service import SystemService
from backend.services.network_service import NetworkService

from backend.repositories.settings_repository import SettingsRepository

from backend.services.application_service import ApplicationService

class SystemController:

    @staticmethod
    def get_page_data():

        info = SystemService.get_system_info()
        settings = SettingsRepository.load()

        return {
            "page_title": "Sistema",
            "page_subtitle": "Informações da Sonda",
            "hostname": info["hostname"],
            "cpu": info["cpu_percent"],
            "memory": info["memory_percent"],
            "disk": SystemService.get_disk_usage(),
            "interfaces": NetworkService.get_network_interfaces(),
            "uptime": SystemService.get_uptime(),
            "settings": settings,
            "application": ApplicationService.get_application_info()
        }
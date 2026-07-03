from backend.services.system_service import SystemService

from backend.services.application_service import ApplicationService

class DashboardController:

    @staticmethod
    def get_page_data():

        info = SystemService.get_system_info()

        return {
            "page_title": "Dashboard",
            "page_subtitle": "Visão geral da Sonda",
            "hostname": info["hostname"],
            "application": ApplicationService.get_application_info()
        }
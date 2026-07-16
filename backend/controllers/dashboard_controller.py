from backend.services.system_service import SystemService

from backend.services.application_service import ApplicationService

from backend.services.dashboard_service import DashboardService


class DashboardController:

    @staticmethod
    def get_page_data():

        info = SystemService.get_system_info()

        return {

            "page_title": "Dashboard",

            "page_subtitle": "Visão geral da Sonda",

            "hostname": info["hostname"],

            "wifi_connectivity":
                DashboardService.get_wifi_connectivity(),

            "application":
                ApplicationService.get_application_info()

        }

    @staticmethod
    def get_wifi_connectivity():

        return DashboardService.get_wifi_connectivity()
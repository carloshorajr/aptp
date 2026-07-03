from backend.services.application_service import ApplicationService

class MetricsController:

    @staticmethod
    def get_page_data():

        return {
            "page_title": "Métricas",
            "page_subtitle": "Indicadores coletados",
            "application": ApplicationService.get_application_info()
        }
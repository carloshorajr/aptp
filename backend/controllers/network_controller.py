from backend.services.network_service import NetworkService


class NetworkController:

    @staticmethod
    def get_page_data():

        return {
            "page_title": "Redes",
            "page_subtitle": "Gerenciamento de Rede",
            "networks": NetworkService.get_cached_networks()
        }

    @staticmethod
    def scan():

        return NetworkService.scan_and_cache()
    
    @staticmethod
    def clear():

        NetworkService.clear_cache()
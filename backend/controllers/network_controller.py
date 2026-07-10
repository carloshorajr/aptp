from flask import request

from backend.services.network_service import NetworkService


class NetworkController:

    @staticmethod
    def get_page_data():

        return {
            "networks": NetworkService.get_cached_networks()
        }

    @staticmethod
    def scan():

        return NetworkService.scan_and_cache()
    
    @staticmethod
    def clear():

        NetworkService.clear_cache()
    
    @staticmethod
    def connect():

        data = request.get_json()

        return NetworkService.connect(

            data["ssid"],
            data["password"]

        )
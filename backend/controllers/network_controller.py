from flask import request

from backend.services.network_service import NetworkService

from backend.services.application_service import (
    ApplicationService
)


class NetworkController:

    @staticmethod
    def get_page_data():

        return {

            "networks": NetworkService.get_cached_networks(),

            "application": ApplicationService.get_application_info()

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
    
    @staticmethod
    def disconnect():

        return NetworkService.disconnect()
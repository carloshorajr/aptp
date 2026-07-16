import socket

from backend.core.config import AppConfig

class ApplicationService:

    @staticmethod
    def get_application_info():

        return {
            "name": AppConfig.NAME,
            "full_name": AppConfig.FULL_NAME,
            "version": AppConfig.VERSION,
            "status": AppConfig.STATUS,
            "environment": AppConfig.ENVIRONMENT,
            "hostname": socket.gethostname()
        }
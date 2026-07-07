from backend.repositories.settings_repository import SettingsRepository

from backend.services.system_service import SystemService

from backend.services.application_service import ApplicationService

from backend.services.network_service import NetworkService

class SettingsController:

    @staticmethod
    def get_page_data():

        settings = SettingsRepository.load()
        
        system = SystemService.get_system_info()

        return {
            "page_title": "Configurações",
            "page_subtitle": "Gerenciamento da Sonda",
            "settings": settings,
            "hostname": system["hostname"],
            "application": ApplicationService.get_application_info()
        }
    
    @staticmethod
    def save(form):

        settings = SettingsRepository.load()

        settings.update_from_form(form)

        SettingsRepository.save(settings)
  
    @staticmethod
    def clear():

        settings = SettingsRepository.load()

        settings.cliente = ""
        settings.local = ""
        settings.descricao = ""

        SettingsRepository.save(settings)
    
    @staticmethod
    def scan_wifi():

        return [

                {
                    "ssid": network.ssid,
                    "connected": network.connected,
                    "signal": network.signal,
                    "security": network.security
                }

                for network in NetworkService.scan_wifi()

            ]
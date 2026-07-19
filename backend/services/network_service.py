import psutil, socket, time

from backend.models.network import NetworkInterface
from backend.models.network import WifiNetwork

from backend.services.command_service import CommandService

from backend.services.wifi_connectivity_service import (
    WifiConnectivityService
)

from backend.services.wifi_signal_service import (
    WifiSignalService
)


class NetworkService:

    _cached_networks = []

    @staticmethod
    def get_wifi_ssid(interface):

        try:

            line = CommandService.run(

                [
                    "nmcli",
                    "-t",
                    "-f",
                    "GENERAL.CONNECTION",
                    "device",
                    "show",
                    interface
                ]

            )

            if not line:
                return None

            if ":" in line:

                return line.split(":", 1)[1].strip()

            return line.strip()

        except Exception:

            return None
    
    @staticmethod
    def get_wifi_connected_time(interface="wlan0"):

        ssid = NetworkService.get_wifi_ssid(interface)

        if not ssid:

            return {

                "ssid": None,

                "seconds": None

            }

        timestamp = CommandService.run(

            [
                "nmcli",
                "-g",
                "connection.timestamp",
                "connection",
                "show",
                ssid
            ]

        )

        if not timestamp:

            return {

                "ssid": ssid,

                "seconds": None

            }

        try:

            connected_since = int(timestamp)

        except ValueError:

            return {

                "ssid": ssid,

                "seconds": None

            }

        return {

            "ssid": ssid,

            "seconds": int(time.time()) - connected_since

        }

    @staticmethod
    def get_saved_ssids():

        output = CommandService.run(

            [
                "nmcli",
                "-t",
                "-f",
                "NAME",
                "connection",
                "show"
            ]

        )

        if not output:

            return set()

        saved = set()

        for line in output.splitlines():

            line = line.strip()

            if line:

                saved.add(line)

        return saved
    
    @staticmethod
    def connect_saved_network(ssid):

        result = CommandService.run_raw(

            [
                "nmcli",
                "connection",
                "up",
                "id",
                ssid
            ]

        )

        return result
    
    @staticmethod
    def update_saved_password(
        ssid,
        password
    ):

        result = CommandService.run_raw(

            [
                "nmcli",
                "connection",
                "modify",
                ssid,
                "wifi-sec.psk",
                password
            ]

        )

        return result

    @staticmethod
    def disconnect():

        result = CommandService.run_raw(

            [
                "nmcli",
                "device",
                "disconnect",
                "wlan0"
            ]

        )

        if result.returncode == 0:

            WifiConnectivityService.collect()

            WifiSignalService.collect_now()

        return {

            "success": result.returncode == 0,

            "message": (

                "Desconectado da rede WiFi."

                if result.returncode == 0

                else result.stderr.strip()

            )

        }

    @staticmethod
    def connection_exists(ssid):

        output = CommandService.run(

            [
                "nmcli",
                "-t",
                "-f",
                "NAME",
                "connection",
                "show"
            ]

        )

        if not output:

            return False

        return ssid in output.splitlines()
    
    @staticmethod
    def get_network_interfaces():

        interfaces = []

        ignored = (
            "lo",
            "docker",
            "br-",
            "veth"
        )

        addrs = psutil.net_if_addrs()

        stats = psutil.net_if_stats()

        for name, addresses in addrs.items():

            if name.startswith(ignored):
                continue

            ip = None
            mac = None

            for addr in addresses:

                if addr.family == socket.AF_INET:

                    ip = addr.address

                elif addr.family == psutil.AF_LINK:

                    mac = addr.address

            if not ip:
                continue

            if name.startswith("eth"):
                interface_type = "Ethernet"

            elif name.startswith("wlan"):
                interface_type = "Wi-Fi"

            else:
                interface_type = "Interface"

            ssid = None

            if name.startswith("wlan"):

                ssid = NetworkService.get_wifi_ssid(name)

            interfaces.append(

                NetworkInterface(

                    interface=name,

                    description=interface_type,

                    ip=ip,

                    mac=mac,

                    ssid=ssid

                )

            )

        return interfaces
    
    @staticmethod
    def scan_wifi():

        output = CommandService.run(

            [
                "nmcli",
                "-t",
                "-f",
                "ACTIVE,SSID,FREQ,CHAN,SIGNAL,SECURITY",
                "device",
                "wifi",
                "list"
            ]

        )

        if not output:

            return []
        
        saved_ssids = NetworkService.get_saved_ssids()

        networks = []

        for line in output.splitlines():

            parts = line.split(":")

            if len(parts) < 6:
                continue

            active = parts[0] == "yes"

            ssid = parts[1].strip()

            if not ssid:

                continue

            frequency_text = parts[2].replace(" MHz", "").strip()

            frequency = int(frequency_text) if frequency_text.isdigit() else 0

            channel = int(parts[3]) if parts[3].isdigit() else 0

            signal = int(parts[4]) if parts[4].isdigit() else 0

            security = parts[5].strip()

            saved = ssid in saved_ssids

            if frequency >= 5000:

                band = "5 GHz"

            else:

                band = "2.4 GHz"

            networks.append(

                WifiNetwork(

                    ssid=ssid,

                    signal=signal,

                    security=security,

                    frequency=frequency,

                    channel=channel,

                    connected=active,

                    saved=saved,

                    band=band

                )

            )

        networks.sort(

            key=lambda network: (

                not network.connected,

                network.ssid.lower(),

                0 if network.frequency >= 5000 else 1,

                -network.signal

            )

        )

        return networks
    
    @staticmethod
    def is_network_available(ssid):

        networks = NetworkService.scan_wifi()

        for network in networks:

            if network.ssid == ssid:

                return True

        return False

    @staticmethod
    def wait_for_network(
        ssid,
        attempts=3,
        interval=10
    ):

        for attempt in range(attempts):

            if NetworkService.is_network_available(ssid):

                return True

            if attempt < attempts - 1:

                time.sleep(interval)

        return False
    
    @staticmethod
    def scan_and_cache():

        NetworkService._cached_networks = (
            NetworkService.scan_wifi()
        )

        return NetworkService._cached_networks


    @staticmethod
    def get_cached_networks():

        return NetworkService._cached_networks

    @staticmethod
    def connect(ssid, password):

        password = password.strip()

        if not password:

            return {

                "success": False,

                "message": "Informe a senha da rede Wi-Fi."

            }

        if not NetworkService.wait_for_network(ssid):

            return {

                "success": False,

                "message":
                    "Rede WiFi não encontrada.\nClique em \"Escanear\" e tente novamente."

            }

        if NetworkService.connection_exists(ssid):

            result = NetworkService.update_saved_password(

                ssid,

                password

            )

            if result.returncode != 0:

                return {

                    "success": False,

                    "message": "Senha inválida."

                }

            result = NetworkService.connect_saved_network(

                ssid

            )

            if result.returncode == 0:

                WifiConnectivityService.collect()

                WifiSignalService.collect_now()

                return {

                    "success": True,

                    "message":
                        f"Conectado à rede '{ssid}'."

                }

            error = result.stderr.strip()

            if (

                "Secrets were required" in error

                or

                "802-11-wireless-security" in error

            ):

                error = "Senha inválida. Digite uma senha válida."

            return {

                "success": False,

                "message": error

            }

        result = CommandService.run_raw(

            [
                "nmcli",
                "device",
                "wifi",
                "connect",
                ssid,
                "password",
                password
            ]

        )

        if result.returncode == 0:

            WifiConnectivityService.collect()

            WifiSignalService.collect_now()

        if result.returncode == 0:

            message = result.stdout.strip()

        else:

            message = result.stderr.strip()

            if (

                "Secrets were required" in message

                or

                "802-11-wireless-security" in message

            ):

                message = "Senha inválida. Digite uma senha válida."

        return {

            "success": result.returncode == 0,

            "message": message

        }

    @staticmethod
    def clear_cache():

        NetworkService._cached_networks = []
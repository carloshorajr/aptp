import psutil
import socket

from backend.models.network import NetworkInterface
from backend.models.network import WifiNetwork

from backend.services.command_service import CommandService

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

        networks = []

        for line in output.splitlines():

            parts = line.split(":")

            if len(parts) < 6:
                continue

            active = parts[0] == "yes"

            ssid = parts[1].strip()

            if not ssid:

                continue

            frequency = int(parts[2].split()[0])

            channel = int(parts[3]) if parts[3].isdigit() else 0

            signal = int(parts[4]) if parts[4].isdigit() else 0

            security = parts[5]

            networks.append(

                WifiNetwork(

                    ssid=ssid,

                    signal=signal,

                    security=security,

                    frequency=frequency,

                    channel=channel,

                    connected=active

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
    def scan_and_cache():

        NetworkService._cached_networks = (
            NetworkService.scan_wifi()
        )

        return NetworkService._cached_networks


    @staticmethod
    def get_cached_networks():

        return NetworkService._cached_networks
    
    @staticmethod
    def clear_cache():

        NetworkService._cached_networks = []
from dataclasses import dataclass

@dataclass
class NetworkInterface:

    interface: str      # eth0, wlan0

    description: str    # Ethernet, Wi-Fi

    ip: str | None

    mac: str | None

    ssid: str | None

@dataclass
class WifiNetwork:

    ssid: str

    signal: int

    security: str

    frequency: int

    channel: int

    connected: bool
from dataclasses import dataclass

@dataclass
class NetworkInterface:

    interface: str

    description: str

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

    saved: bool

    band: str
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

    @property
    def band(self):

        return "5 GHz" if self.frequency >= 5000 else "2.4 GHz"
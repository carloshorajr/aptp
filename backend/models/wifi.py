from dataclasses import dataclass
from datetime import datetime


@dataclass
class Wifi:

    connected: bool

    ssid: str | None

    started_at: datetime | None

    last_seen: datetime | None

    connected_time: int | None

    event: str | None = None
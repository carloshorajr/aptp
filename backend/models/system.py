from dataclasses import dataclass

@dataclass
class SystemInfo:

    hostname: str

    uptime: str

    cpu: float

    memory: float

    disk_used: float

    disk_total: float

    disk_percent: float
import psutil
import socket
from datetime import datetime

from backend.services.network_service import NetworkService

class SystemService:

    @staticmethod
    def get_system_info():

        uptime_seconds = int(
            psutil.boot_time()
        )

        hostname = socket.gethostname()

        return {

            "hostname": hostname,

            "cpu_percent": psutil.cpu_percent(),

            "memory_percent":
                round(
                    psutil.virtual_memory().percent,
                    1
                ),

            "disk_percent":
                round(
                    psutil.disk_usage("/").percent,
                    1
                ),

            "boot_time": uptime_seconds
        }

    @staticmethod
    def get_uptime():

        boot = datetime.fromtimestamp(
            psutil.boot_time()
        )

        delta = datetime.now() - boot

        days = delta.days

        hours = delta.seconds // 3600

        minutes = (
            delta.seconds % 3600
        ) // 60

        if days > 0:

            return f"{days}d {hours}h {minutes}min"

        return f"{hours}h {minutes}min"
    
    @staticmethod
    def get_disk_usage():

        usage = psutil.disk_usage("/")

        total = round(usage.total / (1024 ** 3), 1)

        used = round(usage.used / (1024 ** 3), 1)

        free = round(usage.free / (1024 ** 3), 1)

        return {

            "percent": round(usage.percent, 1),

            "used": used,

            "free": free,

            "total": total

        }
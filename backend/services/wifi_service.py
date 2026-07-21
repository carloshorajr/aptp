from backend.services.command_service import CommandService

from backend.models.wifi import Wifi

from backend.utils.datetime_utils import now


class WifiService:

    @staticmethod
    def collect():

        connected = False

        ssid = None
        
        bssid = None

        connected_time = None

        signal_dbm = None

        output = CommandService.run(

            "iw dev wlan0 link"

        )

        if output:

            lines = output.splitlines()

            for line in lines:

                line = line.strip()

                if line.startswith("Connected to"):

                    connected = True

                    bssid = (

                        line.replace(

                            "Connected to",

                            ""

                        )

                        .split("(")[0]

                        .strip()

                    )

                elif line.startswith("SSID:"):

                    ssid = line.replace(

                        "SSID:",

                        ""

                    ).strip()
                
                elif line.startswith("signal:"):

                    signal_dbm = int(

                        line

                        .replace(

                            "signal:",

                            ""

                        )

                        .replace(

                            "dBm",

                            ""

                        )

                        .strip()

                    )

                elif line.startswith("connected time:"):

                    connected_time = int(

                        line.replace(

                            "connected time:",

                            ""

                        )

                        .replace("seconds", "")

                        .strip()

                    )

        return Wifi(

            connected=connected,

            ssid=ssid,

            bssid=bssid,

            signal_dbm=signal_dbm,

            connected_time=connected_time,

            started_at=None,

            last_seen=now()

        )
    
    @staticmethod
    def collect_latency():

        gateway = None

        routes = CommandService.run(

            "ip route"

        )

        if routes:

            for line in routes.splitlines():

                parts = line.split()

                if (

                    len(parts) >= 5

                    and

                    parts[0] == "default"

                    and

                    parts[1] == "via"

                    and

                    parts[3] == "dev"

                    and

                    parts[4] == "wlan0"

                ):

                    gateway = parts[2]

                    break

        if not gateway:

            return None

        output = CommandService.run(

            [

                "ping",

                "-I",

                "wlan0",

                "-c",

                "10",

                gateway

            ]

        )

        if not output:

            return None

        return {

            "gateway": gateway.strip(),

            "output": output

        }
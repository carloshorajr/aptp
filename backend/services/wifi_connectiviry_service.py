from backend.services.wifi_association_service import (
    WifiAssociationService
)

from backend.services.wifi_station_service import (
    WifiStationService
)


class WifiConnectivityService:

    _previous = None

    @classmethod
    def collect(cls):

        association = WifiAssociationService.collect()

        station = WifiStationService.collect()

        current = {

            "connected": association.connected,

            "ssid": association.ssid,

            "connected_time": station.connected_time

        }

        result = {

            "connected": current["connected"],

            "ssid": current["ssid"],

            "connected_time": current["connected_time"],

            "event": None

        }

        if cls._previous is not None:

            #
            # Primeira associação
            #

            if (

                not cls._previous["connected"]

                and

                current["connected"]

            ):

                result["event"] = "associated"

            #
            # Desassociação
            #

            elif (

                cls._previous["connected"]

                and

                not current["connected"]

            ):

                result["event"] = "disassociated"

            #
            # Reassociação
            #

            elif (

                cls._previous["connected"]

                and

                current["connected"]

                and

                current["ssid"] == cls._previous["ssid"]

                and

                current["connected_time"] is not None

                and

                cls._previous["connected_time"] is not None

                and

                current["connected_time"] < cls._previous["connected_time"]

            ):

                result["event"] = "reassociated"

        cls._previous = current

        return result
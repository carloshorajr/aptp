from datetime import timedelta

from backend.utils.datetime_utils import now

from backend.models.event import Event

from backend.repositories.event_repository import EventRepository

from backend.constants.event_constants import EVENT_SOURCES


class EventService:

    @staticmethod
    def system_started():

        EventService.info(
            "Sistema",
            "Sonda iniciada."
        )

    @staticmethod
    def system_stopped():

        EventService.info(
            "Sistema",
            "Sonda encerrada."
        )

    @staticmethod
    def info(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="INFO",
                source=source,
                message=message
            )
        )
    
    @staticmethod
    def warning(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="WARNING",
                source=source,
                message=message
            )
        )


    @staticmethod
    def error(source: str, message: str):

        EventRepository.add(
            Event(
                timestamp=now(),
                level="ERROR",
                source=source,
                message=message
            )
        )
    
    @staticmethod
    def list(filters=None):

        if filters is None:

            filters = {}

        filters_sql = []

        params = []

        level = filters.get("level")

        if level:

            filters_sql.append(
                "level = ?"
            )

            params.append(level)

        source = filters.get("source")

        if source:

            filters_sql.append(
                "source = ?"
            )

            params.append(source)

        search = filters.get("search")

        if search:

            filters_sql.append(
                "(message LIKE ? OR source LIKE ?)"
            )

            texto = f"%{search}%"

            params.extend([
                texto,
                texto
            ])

        period = filters.get("period")

        if period == "today":

            limite = now().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )

            filters_sql.append(
                "timestamp >= ?"
            )

            params.append(
                limite.isoformat()
            )

        elif period == "24h":

            limite = now() - timedelta(hours=24)

            filters_sql.append(
                "timestamp >= ?"
            )

            params.append(
                limite.isoformat()
            )

        elif period == "7d":

            limite = now() - timedelta(days=7)

            filters_sql.append(
                "timestamp >= ?"
            )

            params.append(
                limite.isoformat()
            )
        
        limit = filters.get("limit", "20")

        if limit == "all":

            limit = None

        else:

            limit = int(limit)

        events = EventRepository.load(

            filters_sql=" AND ".join(filters_sql)
            if filters_sql
            else None,

            params=params,

            limit=limit

        )

        return events
    
    @staticmethod
    def sources():

        return EVENT_SOURCES
    
    @staticmethod
    def statistics():

        events = EventRepository.load()

        total = len(events)

        info = sum(
            1
            for event in events
            if event.level == "INFO"
        )

        warning = sum(
            1
            for event in events
            if event.level == "WARNING"
        )

        error = sum(
            1
            for event in events
            if event.level == "ERROR"
        )

        limite_24h = now() - timedelta(hours=24)

        last_24h = sum(
            1
            for event in events
            if event.timestamp >= limite_24h
        )

        inicio_hoje = now().replace(
            hour=0,
            minute=0,
            second=0,
            microsecond=0
        )

        today = sum(
            1
            for event in events
            if event.timestamp >= inicio_hoje
        )

        return {

            "total": total,

            "info": info,

            "warning": warning,

            "error": error,

            "last_24h": last_24h,

            "today": today

        }
    
    @staticmethod
    def clear():

        EventRepository.clear()
from backend.utils.datetime_utils import now

from backend.models.event import Event
from backend.repositories.event_repository import EventRepository

from datetime import timedelta

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

        events = EventRepository.load()

        if filters is None:
            return events

        period = filters.get("period")

        if period == "today":

            limite = now().replace(
                hour=0,
                minute=0,
                second=0,
                microsecond=0
            )

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        elif period == "24h":

            limite = now() - timedelta(hours=24)

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        elif period == "7d":

            limite = now() - timedelta(days=7)

            events = [
                event
                for event in events
                if event.timestamp >= limite
            ]

        level = filters.get("level")

        if level:

            events = [
                event
                for event in events
                if event.level == level
            ]
        
        source = filters.get("source")

        if source:

            events = [
                event
                for event in events
                if event.source == source
            ]

        search = filters.get("search")

        if search:

            texto = search.lower()

            events = [
                event
                for event in events
                if (
                    texto in event.message.lower()
                    or
                    texto in event.source.lower()
                )
            ]

        return events
    
    @staticmethod
    def sources():

        events = EventRepository.load()

        return sorted(
            {
                event.source
                for event in events
            }
        )
    
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
from datetime import datetime
from zoneinfo import ZoneInfo

from backend.repositories.settings_repository import SettingsRepository


def get_timezone():

    settings = SettingsRepository.load()

    return ZoneInfo(settings.timezone)


def now():

    return datetime.now(get_timezone())


def parse_datetime(value: str):

    dt = datetime.fromisoformat(value)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=get_timezone())

    return dt
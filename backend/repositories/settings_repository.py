import json

from dataclasses import asdict

from backend.models.settings import Settings

from backend.utils.identity import generate_uuid

from backend.core.paths import SETTINGS_FILE

class SettingsRepository:

    @classmethod
    def load(cls):

        if not SETTINGS_FILE.exists():
            return cls.create_default()

        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        settings = Settings(**data)

        if not settings.uuid:
            settings.uuid = generate_uuid()
            cls.save(settings)

        return settings

    @classmethod
    def save(cls, settings: Settings):

        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(
                asdict(settings),
                f,
                indent=4,
                ensure_ascii=False
            )
    
    @classmethod
    def create_default(cls):

        settings = Settings(
            nome="Sonda",
            cliente="",
            local="",
            descricao="",
            uuid=generate_uuid(),
            heartbeat=60,
            coleta=30,
            timezone="America/Sao_Paulo",
            idioma="pt-BR",
            log_level="INFO"
        )

        cls.save(settings)

        return settings
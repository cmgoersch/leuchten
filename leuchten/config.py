from dataclasses import dataclass
from os import getenv


@dataclass
class Settings:
    prometheus_host: str = getenv('PROMETHEUS_URL') or ''


settings = Settings()

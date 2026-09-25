import os
from dataclasses import dataclass


class ConfigError(ValueError):
    pass


def required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ConfigError(f"Missing required environment variable: {name}")
    return value


@dataclass(frozen=True)
class Config:
    latitude: float
    longitude: float
    uv_threshold: float
    forecast_days: int
    notification_hour: int
    telegram_bot_token: str
    telegram_chat_id: str

    @classmethod
    def from_env(cls) -> "Config":
        try:
            latitude = float(required("LATITUDE"))
            longitude = float(required("LONGITUDE"))
            uv_threshold = float(os.getenv("UV_THRESHOLD", "5"))
            forecast_days = int(os.getenv("FORECAST_DAYS", "7"))
            notification_hour = int(required("NOTIFICATION_HOUR"))
        except ValueError as exc:
            raise ConfigError("Invalid numeric configuration") from exc
        if not -90 <= latitude <= 90:
            raise ConfigError("LATITUDE must be between -90 and 90")
        if not -180 <= longitude <= 180:
            raise ConfigError("LONGITUDE must be between -180 and 180")
        if uv_threshold < 0:
            raise ConfigError("UV_THRESHOLD must be >= 0")
        if not 1 <= forecast_days <= 16:
            raise ConfigError("FORECAST_DAYS must be between 1 and 16")
        if not 0 <= notification_hour <= 23:
            raise ConfigError("NOTIFICATION_HOUR must be between 0 and 23")
        return cls(latitude, longitude, uv_threshold, forecast_days, notification_hour,
                   required("TELEGRAM_BOT_TOKEN"), required("TELEGRAM_CHAT_ID"))

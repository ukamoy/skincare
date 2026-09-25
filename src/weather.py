from dataclasses import dataclass
from datetime import date
from typing import Any
import requests

URL = "https://api.open-meteo.com/v1/forecast"


class WeatherError(RuntimeError):
    pass


@dataclass(frozen=True)
class DailyUV:
    day: date
    uv_index: float


@dataclass(frozen=True)
class Forecast:
    timezone: str
    latitude: float
    longitude: float
    daily: list[DailyUV]


def fetch_forecast(latitude: float, longitude: float, forecast_days: int) -> Forecast:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "uv_index_max",
        "forecast_days": forecast_days,
        "timezone": "auto",
    }
    try:
        r = requests.get(URL, params=params, timeout=20)
        r.raise_for_status()
        payload: dict[str, Any] = r.json()
    except requests.RequestException as exc:
        raise WeatherError(f"Open-Meteo request failed: {exc}") from exc
    if payload.get("error"):
        raise WeatherError(str(payload.get("reason", "Open-Meteo error")))
    try:
        daily = [
            DailyUV(date.fromisoformat(d), float(u))
            for d, u in zip(payload["daily"]["time"], payload["daily"]["uv_index_max"])
            if u is not None
        ]
        return Forecast(
            timezone=payload["timezone"],
            latitude=float(payload["latitude"]),
            longitude=float(payload["longitude"]),
            daily=daily,
        )
    except (KeyError, TypeError, ValueError) as exc:
        raise WeatherError("Unexpected Open-Meteo response") from exc

import os
from datetime import datetime
from zoneinfo import ZoneInfo

from config import Config
from telegram import send_message
from weather import fetch_forecast


def uv_level(uv: float) -> str:
    if uv < 3:
        return "Low"
    if uv < 6:
        return "Moderate"
    if uv < 8:
        return "High"
    if uv < 11:
        return "Very High"
    return "Extreme"


def build_message(forecast, threshold: float) -> str:
    risky = [x for x in forecast.daily if x.uv_index >= threshold]
    lines = [
        "☀️ UV Alert", "",
        f"Location: {forecast.latitude:.4f}, {forecast.longitude:.4f}",
        f"Timezone: {forecast.timezone}",
        f"Threshold: UV Index ≥ {threshold:g}", "",
    ]
    for item in risky:
        lines.append(f"{item.day.isoformat()}: UV {item.uv_index:g} ({uv_level(item.uv_index)})")
    lines += ["", "Source: Open-Meteo", "Daily maximum UV forecast."]
    return "\n".join(lines)


def is_notification_hour(timezone: str, notification_hour: int, now: datetime | None = None) -> bool:
    if now is None:
        now = datetime.now(ZoneInfo(timezone))
    return now.hour == notification_hour


def main() -> int:
    config = Config.from_env()
    forecast = fetch_forecast(config.latitude, config.longitude, config.forecast_days)
    force_alert = os.getenv("FORCE_ALERT", "").lower() == "true"
    if not force_alert and not is_notification_hour(forecast.timezone, config.notification_hour):
        print(f"Not the configured notification hour in {forecast.timezone}.")
        return 0
    risky = [x for x in forecast.daily if x.uv_index >= config.uv_threshold]
    if not risky:
        print(f"No UV alert for the next {config.forecast_days} days.")
        return 0
    send_message(config.telegram_bot_token, config.telegram_chat_id,
                 build_message(forecast, config.uv_threshold))
    print(f"Sent UV alert for {len(risky)} day(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

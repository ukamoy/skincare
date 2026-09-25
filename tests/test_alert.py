from datetime import date, datetime
from zoneinfo import ZoneInfo

from main import build_message, is_notification_hour
from weather import DailyUV, Forecast


def test_message():
    f = Forecast("America/Toronto", 43.65, -79.38, [DailyUV(date(2026, 6, 1), 7)])
    m = build_message(f, 5)
    assert "UV 7" in m
    assert "High" in m


def test_notification_hour():
    timezone = ZoneInfo("America/Toronto")
    matching_time = datetime(2026, 6, 1, 8, 17, tzinfo=timezone)
    other_time = datetime(2026, 6, 1, 9, 17, tzinfo=timezone)

    assert is_notification_hour("America/Toronto", 8, matching_time)
    assert not is_notification_hour("America/Toronto", 8, other_time)

from datetime import date, datetime

from main import build_message, is_notification_hour
from weather import DailyUV, Forecast


def test_message():
    f = Forecast("America/Toronto", 43.65, -79.38, [DailyUV(date(2026, 6, 1), 7)])
    m = build_message(f, 5)
    assert "UV 7" in m
    assert "High" in m


def test_notification_hour():
    assert is_notification_hour("America/Toronto", 8, datetime(2026, 6, 1, 8, 17))
    assert not is_notification_hour("America/Toronto", 8, datetime(2026, 6, 1, 9, 17))

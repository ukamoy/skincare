from datetime import date
from main import build_message
from weather import DailyUV, Forecast


def test_message():
    f = Forecast("America/Toronto", 43.65, -79.38, [DailyUV(date(2026, 6, 1), 7)])
    m = build_message(f, 5)
    assert "UV 7" in m
    assert "High" in m

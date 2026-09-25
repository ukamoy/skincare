import pytest

from config import Config, ConfigError


def test_config(monkeypatch):
    for k, v in {
        "LATITUDE": "43.65", "LONGITUDE": "-79.38", "UV_THRESHOLD": "5",
        "FORECAST_DAYS": "7", "TELEGRAM_BOT_TOKEN": "x", "TELEGRAM_CHAT_ID": "1"
    }.items():
        monkeypatch.setenv(k, v)
    c = Config.from_env()
    assert c.latitude == 43.65
    assert c.uv_threshold == 5


def test_bad_latitude(monkeypatch):
    monkeypatch.setenv("LATITUDE", "100")
    monkeypatch.setenv("LONGITUDE", "0")
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "x")
    monkeypatch.setenv("TELEGRAM_CHAT_ID", "1")
    with pytest.raises(ConfigError):
        Config.from_env()

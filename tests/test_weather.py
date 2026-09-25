from weather import fetch_forecast


class Response:
    def raise_for_status(self): pass
    def json(self):
        return {"latitude": 43.65, "longitude": -79.38, "timezone": "America/Toronto",
                "daily": {"time": ["2026-06-01"], "uv_index_max": [7]}}


def test_fetch(monkeypatch):
    monkeypatch.setattr("weather.requests.get", lambda *a, **k: Response())
    f = fetch_forecast(43.65, -79.38, 1)
    assert f.timezone == "America/Toronto"
    assert f.daily[0].uv_index == 7

# UV Alert

Daily UV forecast notifications using GitHub Actions, Open-Meteo, and Telegram.

## Configuration

In repository **Settings -> Secrets and variables -> Actions**, add these repository variables:

| Variable | Example | Description |
| --- | ---: | --- |
| `LATITUDE` | `43.6532` | WGS84 latitude |
| `LONGITUDE` | `-79.3832` | WGS84 longitude |
| `NOTIFICATION_HOUR` | `7` | Local hour from 0 through 23 |
| `UV_THRESHOLD` | `5` | Alert when daily maximum UV meets this value |
| `FORECAST_DAYS` | `7` | Number of forecast days, from 1 through 16 |

Add these repository secrets:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

No timezone variable or personal access token is required. Open-Meteo resolves the timezone from the configured coordinates.

## Workflows

Run **Validate UV Alert Settings** manually after changing a location or notification hour. It checks the configuration and reports the resolved timezone.

**UV Alert** runs hourly at minute 17. It checks the current hour in the resolved local timezone and sends an alert only when it matches `NOTIFICATION_HOUR`. Run it manually for an immediate Telegram test.

## UV logic

The application requests Open-Meteo's daily `uv_index_max`. If no day reaches `UV_THRESHOLD`, no Telegram message is sent. If multiple days meet the threshold, they are included in one message.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
ruff check src tests
```

## Structure

```text
uv-alert/
|-- .github/workflows/
|   |-- ci.yml
|   |-- setup.yml
|   `-- uv-alert.yml
|-- src/
|-- tests/
|-- pyproject.toml
|-- requirements.txt
`-- requirements-dev.txt
```

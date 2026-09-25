# UV Alert

Alertas UV diarias con GitHub Actions, Open-Meteo y Telegram.

Configure `LATITUDE`, `LONGITUDE`, `NOTIFICATION_HOUR`, `UV_THRESHOLD` y `FORECAST_DAYS` en las Variables del repositorio y ejecute **Actions → Setup UV Alert Schedule → Run workflow**. La zona horaria se obtiene automáticamente desde las coordenadas mediante `timezone=auto` de Open-Meteo. citeturn0search2

Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

GitHub Actions admite schedules con zonas horarias IANA y DST. citeturn0search0

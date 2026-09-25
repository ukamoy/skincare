# UV Alert

Alerte UV quotidienne avec GitHub Actions, Open-Meteo et Telegram.

Configurez `LATITUDE`, `LONGITUDE`, `NOTIFICATION_HOUR`, `UV_THRESHOLD` et `FORECAST_DAYS` dans les Variables du dépôt, puis lancez **Actions → Setup UV Alert Schedule → Run workflow**. Le fuseau horaire est déterminé automatiquement à partir des coordonnées via Open-Meteo `timezone=auto`. citeturn0search2

Secrets : `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

GitHub Actions prend en charge les horaires avec fuseau IANA et DST. citeturn0search0

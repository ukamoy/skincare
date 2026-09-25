# UV Alert

Avvisi UV giornalieri con GitHub Actions, Open-Meteo e Telegram.

Configura `LATITUDE`, `LONGITUDE`, `NOTIFICATION_HOUR`, `UV_THRESHOLD` e `FORECAST_DAYS` nelle Variables del repository, quindi esegui **Actions → Setup UV Alert Schedule → Run workflow**. Il fuso orario viene determinato automaticamente dalle coordinate tramite `timezone=auto` di Open-Meteo. citeturn0search2

Secrets: `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

GitHub Actions supporta schedule con fusi orari IANA e DST. citeturn0search0

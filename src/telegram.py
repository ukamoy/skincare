import requests


class TelegramError(RuntimeError):
    pass


def send_message(bot_token: str, chat_id: str, message: str) -> None:
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    try:
        r = requests.post(url, json={"chat_id": chat_id, "text": message}, timeout=20)
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as exc:
        raise TelegramError(f"Telegram request failed: {exc}") from exc
    if not data.get("ok"):
        raise TelegramError(str(data))

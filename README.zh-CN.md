# UV Alert

基于 GitHub Actions、Open-Meteo 和 Telegram 的每日 UV 预警。

## 配置

GitHub → **Settings → Secrets and variables → Actions**。

Variables：

| 名称 | 示例 | 说明 |
|---|---:|---|
| `LATITUDE` | `43.6532` | 纬度 |
| `LONGITUDE` | `-79.3832` | 经度 |
| `NOTIFICATION_HOUR` | `7` | 当地时间小时，0–23 |
| `UV_THRESHOLD` | `5` | 每日最高 UV 达到此值时通知 |
| `FORECAST_DAYS` | `7` | 预测天数，1–16 |

Secrets：`TELEGRAM_BOT_TOKEN`、`TELEGRAM_CHAT_ID`。

**不需要填写时区。** Setup Workflow 会使用 Open-Meteo 的 `timezone=auto`，根据经纬度自动确定 IANA 时区。citeturn0search2

## 使用

1. 配置 Variables 和 Secrets。
2. 打开 **Actions → Setup UV Alert Schedule → Run workflow**。
3. 自动解析时区并生成 `.github/workflows/uv-alert.yml`。
4. 自动提交生成的 workflow。
5. 在 **Actions → UV Alert → Run workflow** 立即测试。

修改经纬度或通知小时后，再运行一次 Setup。

GitHub Actions 支持带 IANA 时区的 schedule 和 DST。citeturn0search0

## UV

程序使用 Open-Meteo 的每日 `uv_index_max`。`UV_THRESHOLD=5` 表示 UV Index ≥ 5，并不是太阳强度的 50%。citeturn0search2

import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

ADMIN_IDS = {
    int(admin_id)
    for admin_id in os.getenv("ADMIN_IDS", "284929331,1020303972").split(",")
    if admin_id.strip()
}


def validate_bot_config() -> None:
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set. Copy .env.example to .env and fill it.")
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is not set. Add your Dokploy Postgres URL to env.")

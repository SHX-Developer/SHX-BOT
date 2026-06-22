# SHX BOT

Telegram bot on `aiogram` with PostgreSQL, SQL migrations, Docker Compose and CI.
The app expects a PostgreSQL database URL from the environment.

## Local Run

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Fill `BOT_TOKEN`, `ADMIN_IDS` and `DATABASE_URL` in `.env`, then run:

```powershell
python -m scripts.migrate
python main.py
```

## Docker Compose

```bash
cp .env.example .env
docker compose up -d --build
docker compose logs -f bot
```

The bot container applies migrations automatically before polling starts.

## Import Old SQLite Data

After Postgres is available and `.env` is configured:

```bash
python -m scripts.import_sqlite_to_postgres --sqlite ShaHriXMusicBot.db
```

## VPS Deploy

1. Create or connect a PostgreSQL database.
2. Set `BOT_TOKEN`, `ADMIN_IDS` and `DATABASE_URL`.
3. Deploy `docker-compose.yml`.
4. Check logs for `Bot polling started`.

## CI

GitHub Actions runs:

- dependency installation
- Python compile check
- Postgres migrations
- Docker image build

## Repository Notes

Do not commit `.env`, `.venv`, `__pycache__` or `*.db` files. Secrets must stay in environment variables.

# SHX BOT

Telegram bot on `aiogram` with PostgreSQL, SQL migrations, Docker Compose and CI.

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

After Postgres is running and `.env` is configured:

```bash
python -m scripts.import_sqlite_to_postgres --sqlite ShaHriXMusicBot.db
```

## VPS Deploy

1. Install Docker and Docker Compose plugin.
2. Clone the repository on the server.
3. Create `.env` from `.env.example`.
4. Run `docker compose up -d --build`.
5. Check logs with `docker compose logs -f bot`.

## CI

GitHub Actions runs:

- dependency installation
- Python compile check
- Postgres migrations
- Docker image build

## Repository Notes

Do not commit `.env`, `.venv`, `__pycache__` or `*.db` files. Secrets must stay in environment variables.

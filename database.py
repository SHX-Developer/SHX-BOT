import asyncio
import logging
import re
from pathlib import Path
from typing import Any, Sequence

import asyncpg

from config import DATABASE_URL


logger = logging.getLogger(__name__)

MIGRATIONS_DIR = Path(__file__).resolve().parent / "migrations"
_pool: asyncpg.Pool | None = None
_pool_lock = asyncio.Lock()


def _convert_placeholders(query: str) -> str:
    """Convert sqlite-style placeholders to asyncpg placeholders."""
    index = 0

    def replace(_: re.Match[str]) -> str:
        nonlocal index
        index += 1
        return f"${index}"

    return re.sub(r"\?", replace, query)


async def init_db() -> asyncpg.Pool:
    global _pool

    if _pool is not None:
        return _pool

    async with _pool_lock:
        if _pool is None:
            _pool = await asyncpg.create_pool(
                dsn=DATABASE_URL,
                min_size=1,
                max_size=10,
                command_timeout=30,
            )
            logger.info("Postgres connection pool created")

    return _pool


async def close_db() -> None:
    global _pool

    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("Postgres connection pool closed")


async def run_migrations() -> None:
    pool = await init_db()

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                """
                CREATE TABLE IF NOT EXISTS schema_migrations (
                    version TEXT PRIMARY KEY,
                    applied_at TIMESTAMPTZ NOT NULL DEFAULT now()
                )
                """
            )

            applied = {
                row["version"]
                for row in await conn.fetch("SELECT version FROM schema_migrations")
            }

            migration_files = sorted(MIGRATIONS_DIR.glob("*.sql"))
            for migration in migration_files:
                version = migration.name
                if version in applied:
                    continue

                sql = migration.read_text(encoding="utf-8")
                logger.info("Applying migration %s", version)
                await conn.execute(sql)
                await conn.execute(
                    "INSERT INTO schema_migrations (version) VALUES ($1)",
                    version,
                )


async def execute_query(query: str, parameters: Sequence[Any] = ()) -> None:
    pool = await init_db()
    sql = _convert_placeholders(query)

    async with pool.acquire() as conn:
        await conn.execute(sql, *parameters)


async def fetchone_query(
    query: str,
    parameters: Sequence[Any] = (),
) -> tuple[Any, ...] | None:
    pool = await init_db()
    sql = _convert_placeholders(query)

    async with pool.acquire() as conn:
        row = await conn.fetchrow(sql, *parameters)

    return tuple(row) if row is not None else None


async def fetchall_query(
    query: str,
    parameters: Sequence[Any] = (),
) -> list[tuple[Any, ...]]:
    pool = await init_db()
    sql = _convert_placeholders(query)

    async with pool.acquire() as conn:
        rows = await conn.fetch(sql, *parameters)

    return [tuple(row) for row in rows]


async def create_tables() -> None:
    await run_migrations()


async def add_basic_data(
    user_id: int,
    username: str | None,
    firstname: str | None,
    lastname: str | None,
    fullname: str | None,
    language: str | None,
    chat_id: int,
    chat_type: str,
    is_premium: bool | None,
    date: str,
    time: str,
) -> None:
    pool = await init_db()

    async with pool.acquire() as conn:
        async with conn.transaction():
            await conn.execute(
                """
                INSERT INTO user_access (
                    user_id, username, firstname, lastname, fullname, language,
                    chat_id, chat_type, is_premium, date, time
                )
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
                ON CONFLICT (user_id) DO NOTHING
                """,
                user_id,
                username,
                firstname,
                lastname,
                fullname,
                language,
                chat_id,
                chat_type,
                is_premium,
                date,
                time,
            )
            await conn.execute(
                """
                INSERT INTO user_data (user_id, username, language)
                VALUES ($1, $2, '-')
                ON CONFLICT (user_id) DO NOTHING
                """,
                user_id,
                username,
            )

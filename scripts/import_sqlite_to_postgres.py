import argparse
import asyncio
import sqlite3
from collections.abc import Iterable
from pathlib import Path

import asyncpg

from config import DATABASE_URL
from database import close_db, run_migrations


TABLES = ("user_access", "user_data", "russian", "english", "playlists", "new")


def read_rows(db_path: Path, table: str) -> tuple[list[str], list[tuple]]:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table' AND name = ?",
            (table,),
        )
        if cursor.fetchone() is None:
            return [], []

        columns = [row[1] for row in conn.execute(f"PRAGMA table_info({table})")]
        rows = list(conn.execute(f"SELECT {', '.join(columns)} FROM {table}"))
        return columns, rows


def placeholders(count: int) -> str:
    return ", ".join(f"${index}" for index in range(1, count + 1))


def normalize_row(table: str, columns: list[str], row: tuple) -> tuple:
    if table != "user_access" or "is_premium" not in columns:
        return row

    values = list(row)
    index = columns.index("is_premium")
    value = values[index]
    if value in {None, "", "0", 0, False}:
        values[index] = False
    elif value in {"1", 1, True, "true", "True"}:
        values[index] = True
    return tuple(values)


async def insert_rows(
    conn: asyncpg.Connection,
    table: str,
    columns: list[str],
    rows: Iterable[tuple],
) -> int:
    if not columns:
        return 0

    column_sql = ", ".join(columns)
    conflict_sql = " ON CONFLICT (user_id) DO NOTHING" if table in {"user_access", "user_data"} else ""
    if table == "new":
        conflict_sql = " ON CONFLICT (callback) DO NOTHING"

    query = (
        f"INSERT INTO {table} ({column_sql}) "
        f"VALUES ({placeholders(len(columns))})"
        f"{conflict_sql}"
    )

    count = 0
    for row in rows:
        await conn.execute(query, *normalize_row(table, columns, row))
        count += 1
    return count


async def refresh_sequence(conn: asyncpg.Connection, table: str) -> None:
    if table in {"user_access", "user_data"}:
        return

    await conn.execute(
        """
        SELECT setval(
            pg_get_serial_sequence($1, 'id'),
            COALESCE((SELECT MAX(id) FROM """ + table + """), 1),
            true
        )
        """,
        table,
    )


async def main() -> None:
    parser = argparse.ArgumentParser(description="Import legacy SQLite data to Postgres.")
    parser.add_argument(
        "--sqlite",
        default="ShaHriXMusicBot.db",
        help="Path to legacy SQLite database.",
    )
    args = parser.parse_args()
    sqlite_path = Path(args.sqlite)

    if not sqlite_path.exists():
        raise FileNotFoundError(f"SQLite database not found: {sqlite_path}")

    await run_migrations()
    pg = await asyncpg.connect(DATABASE_URL)

    try:
        async with pg.transaction():
            for table in TABLES:
                columns, rows = read_rows(sqlite_path, table)
                imported = await insert_rows(pg, table, columns, rows)
                await refresh_sequence(pg, table)
                print(f"{table}: imported {imported} rows")
    finally:
        await pg.close()
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())

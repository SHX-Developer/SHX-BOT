import asyncio
import logging

from database import close_db, run_migrations


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)


async def main() -> None:
    await run_migrations()
    await close_db()


if __name__ == "__main__":
    asyncio.run(main())

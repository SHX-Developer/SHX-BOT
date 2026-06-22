import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from admin.router import router as admin_router
from config import TOKEN, validate_bot_config
from database import close_db, run_migrations
from handlers import router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)
logger = logging.getLogger(__name__)


async def main() -> None:
    validate_bot_config()
    await run_migrations()

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(
            parse_mode="HTML",
            link_preview_is_disabled=False,
        ),
    )
    dp = Dispatcher()
    dp.include_router(admin_router)
    dp.include_router(router)

    try:
        logger.info("Bot polling started")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await close_db()


if __name__ == "__main__":
    asyncio.run(main())

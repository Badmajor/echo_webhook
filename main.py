import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

from config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_PORT, WEBAPP_HOST
from handlers import register_routers

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)

    router = Router()

    register_routers(router)

    dp = Dispatcher()
    dp.include_router(router)

    aiohttp_logger = logging.getLogger("aiohttp.access")
    aiohttp_logger.setLevel(logging.CRITICAL)

    # Setting webhook
    await bot.set_webhook(
        url=WEBHOOK_URL,
        drop_pending_updates=True,
        allowed_updates=dp.resolve_used_update_types()
    )

    # Running it forever
    await asyncio.Event().wait()
    await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

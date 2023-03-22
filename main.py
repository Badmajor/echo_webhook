import asyncio
import logging
from aiogram import Bot, Dispatcher, Router

from config import BOT_TOKEN
from handlers import register_routers

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)

    router = Router()

    register_routers(router)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())

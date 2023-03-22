from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message


async def cmd_start(message: Message):
    await message.answer('Привет, мир!')


def register_routers(router: Router):
    router.message.register(cmd_start, Command(commands="start"))

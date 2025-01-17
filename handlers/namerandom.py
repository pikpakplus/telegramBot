from aiogram import Router, types
from aiogram.filters import Command
import random

namerandom_router = Router()

Names = ("Адыл", "Асан", "Ислам", "Тимур", "Рома", "Дима")


@namerandom_router.message(Command('random'))
async def random_name_handler(message: types.Message):
    random_name = random.choice(Names)
    await message.answer(f"рандомное имя: {random_name}")

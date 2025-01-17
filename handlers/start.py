from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://"
                                                                                  "geeks.kg"),
                types.InlineKeyboardButton(text="Оставь отзыв", callback_data="review:start")

            ]

        ]

    )
    await message.reply(f"Привет, {name}! Добро пожаловать на наш бот.", reply_markup=kb)
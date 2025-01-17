from aiogram import Router, types

echo_messege_router = Router()


@echo_messege_router.message()
async def echo_handler(message: types.Message):
    await message.answer("Попробуй вставить это: /start, /myinfo, /random")
import asyncio
import logging
from handlers.start import start_router
from handlers.echo_messege import echo_messege_router
from config_bot import bot, dp
from handlers.info import info_router
from handlers.namerandom import namerandom_router
from handlers.review_dialog import review_router


async def main():
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(namerandom_router)
    dp.include_router(review_router)
    dp.include_router(echo_messege_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

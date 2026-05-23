import asyncio
import logging
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import register_routes
from keyboards.commands import set_bot_commands

# Находим файл .env и загружаем из него переменные окружения
load_dotenv()

# Забираем токен.
TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    register_routes(dp)

    await set_bot_commands(bot)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        print("Bot is running...")
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Bot stopped")
    except Exception as e:
        print(e)

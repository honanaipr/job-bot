from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, CommandObject
from aiogram.types import Message
import os
import re
import asyncio
from loguru import logger

TOKEN = os.getenv("BOT_TOKEN") or ""

if not TOKEN:
    logger.error("BOT_TOKEN not set")
    exit(1)

if not re.findall(r"/^[0-9]{8,10}:[a-zA-Z0-9_-]{35}$/", TOKEN):
    logger.error("BOT_TOKEN invalid")
    exit(1)

dp = Dispatcher()

@dp.message(CommandStart())
def start_handler(message: Message, command: CommandObject):
    logger.info(command)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Router, types, Bot
from aiogram.filters import Command
from keyboards.commands import get_bot_commands

router = Router()


@router.message(Command("help"))
async def help_command(message: types.Message, bot: Bot):
    text = await get_bot_commands(bot)

    await message.answer(f"Доступные команды:\n\n{text}")

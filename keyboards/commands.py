from aiogram import Bot
from aiogram.types import BotCommand
from data.questions_data import COMMANDS


async def set_bot_commands(bot: Bot):
    commands_list = []
    for COMMAND, DESCRIPTION in COMMANDS.items():
        commands_list.append(BotCommand(command=COMMAND, description=DESCRIPTION))

    await bot.set_my_commands(commands_list)


async def get_bot_commands(bot: Bot) -> str:
    commands = await bot.get_my_commands()

    if not commands:
        return

    commands_text = ""
    for cmd in commands:
        commands_text += f"/{cmd.command} - {cmd.description}\n"

    return commands_text

from aiogram import F, Router, types
from data.questions_data import HANDLERS, COMMANDS

router = Router()


@router.message(~F.text.in_(HANDLERS), ~F.text.startswith("/"))
async def input_error(message: types.Message):
    await message.answer("Упс...\n"
                         "Кажется я вас не понял, если вы хотите посмотреть список доступных команд нажмите /help")

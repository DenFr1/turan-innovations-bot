from aiogram import F, Router, types
from data.questions_data import HANDLERS

router = Router()


@router.message(~F.text.in_(HANDLERS))
async def input_error(message: types.Message):
    await message.answer("Упс...\n"
                         "Кажется я вас не понял, если вы хотите посмотреть список доступных команд нажмите /help")

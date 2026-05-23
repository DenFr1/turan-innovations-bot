from aiogram import F, Router, types
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.keyboards import generate_faq_keyboard
from data.questions_data import PARTICIPATION_DATA

router = Router()

PREFIX = "part"


@router.message(F.text == "Кто может участвовать")
async def criteria(message: types.Message):
    text = "<b>Выберите интересующий вас вопрос:</b>\n\n"

    for key, value in PARTICIPATION_DATA.items():
        text += f"{key}. {value['q']}\n"

    await message.answer(
        text,
        reply_markup=generate_faq_keyboard(PARTICIPATION_DATA, PREFIX),
        parse_mode="HTML"
    )


@router.callback_query(F.data.startswith(f"{PREFIX}:"))
async def info_callback(callback: CallbackQuery):
    item_id = callback.data.split(":")[1]

    if item_id == "back":
        text = "<b>Выберите интересующий вас вопрос:</b>\n\n"
        for key, value in PARTICIPATION_DATA.items():
            text += f"{key}. {value['q']}\n"

        await callback.message.edit_text(
            text=text,
            reply_markup=generate_faq_keyboard(PARTICIPATION_DATA, PREFIX),
            parse_mode="HTML"
        )
        await callback.answer()
        return

    answer_text = PARTICIPATION_DATA[item_id]["a"]

    back_button = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад к вопросам", callback_data=f"{PREFIX}:back")]
    ])

    await callback.message.edit_text(text=answer_text, reply_markup=back_button)
    await callback.answer()

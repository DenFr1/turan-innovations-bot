from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def generate_faq_keyboard(data_dict: dict, prefix: str):
    builder = InlineKeyboardBuilder()

    for key in data_dict.keys():
        builder.add(InlineKeyboardButton(
            text=key,
            callback_data=f"{prefix}:{key}"
        ))

    builder.adjust(4)
    return builder.as_markup()

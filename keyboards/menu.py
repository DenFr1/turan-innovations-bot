from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О конкурсе")],
            [KeyboardButton(text="Кто может участвовать"), KeyboardButton(text="Правила и подача")],
            [KeyboardButton(text="Этапы и критерии")]
        ],
        resize_keyboard=True
    )

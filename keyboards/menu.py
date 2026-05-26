from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="О конкурсе")],
            [KeyboardButton(text="Кто может участвовать"), KeyboardButton(text="Этапы и критерии"), KeyboardButton(text="Правила и подача")],
            [KeyboardButton(text="Контакты")]
        ],
        resize_keyboard=True
    )

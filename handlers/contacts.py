from aiogram import F, Router, types

router = Router()


@router.message(F.text == "Контакты")
async def get_contacts(message: types.Message):
    await message.answer(
        "<b>Контакты организаторов конкурса:</b>\n\n"
        "Береснева Анна Сергеевна\n"
        "+77012100020\n"
        "b-i@turan-edu.kz",
        parse_mode="HTML"
    )

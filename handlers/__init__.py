from aiogram import Dispatcher

from handlers.start import router as start_router
from handlers.info import router as info_router
from handlers.participation import router as participation_router
from handlers.rules_and_admission import router as rules_router
from handlers.criteria import router as criteria_router
from handlers.help import router as help_router
from handlers.input_error import router as input_error_router
from handlers.contacts import router as contacts_router


def register_routes(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(info_router)
    dp.include_router(participation_router)
    dp.include_router(rules_router)
    dp.include_router(criteria_router)
    dp.include_router(help_router)
    dp.include_router(input_error_router)
    dp.include_router(contacts_router)

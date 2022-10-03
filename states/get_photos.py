from aiogram.dispatcher.filters.state import StatesGroup, State


class Photos(StatesGroup):
    get_photos = State()

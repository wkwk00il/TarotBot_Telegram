from aiogram.filters.state import State, StatesGroup


class AdminActions(StatesGroup):
    change_balance = State()
    add_admin = State()
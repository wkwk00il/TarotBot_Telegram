from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Получить расклад'
        ),
        KeyboardButton(
            text='Баланс'
        )
    ]
], resize_keyboard=True, one_time_keyboard=False, )


reply_keyboard_admin = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Получить расклад'
        ),
        KeyboardButton(
            text='Баланс'
        ),
        KeyboardButton(
            text='Админ-панель'
        ),
    ]
], resize_keyboard=True, one_time_keyboard=False, )
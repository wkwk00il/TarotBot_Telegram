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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_type = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Короткий универсальный',
            callback_data='short_uni'
        )
    ],
    [
        InlineKeyboardButton(
            text='Длинный универсальный',
            callback_data='long_uni'
        )
    ],
    [
        InlineKeyboardButton(
            text='Оракул любви',
            callback_data='oracle_love'
        )
    ],
    [
        InlineKeyboardButton(
            text='Триплет',
            callback_data='triple'
        )
    ]
])

select_cash_in = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Пополнить баланс на 150р',
            callback_data='cash_in_150r'
        )
    ],
    [
        InlineKeyboardButton(
            text='Пополнить баланс на 250р',
            callback_data='cash_in_250r'
        )
    ]
])

pay_for_layout_40 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оплатить',
            callback_data='pay_for_40'
        )
    ]
])

pay_for_layout_65 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оплатить',
            callback_data='pay_for_65'
        )
    ]
])

pay_for_layout_80 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оплатить',
            callback_data='pay_for_80'
        )
    ]
])

pay_for_layout_45 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Оплатить',
            callback_data='pay_for_45'
        )
    ]
])
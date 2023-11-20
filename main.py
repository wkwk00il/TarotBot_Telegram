import config
import logging
import openpyxl
from commands import set_commands
import asyncio
from reply import reply_keyboard, reply_keyboard_admin
from inline import select_type, admin_panel_keyboard
from callback import all_callback
import json
from payment import pre_checkout_query
from payment import cash_in_150, cash_in_250
from payment import succ_cash_in_150
from databases import db_table_val, get_user_admin, add_admin
from databases import get_user_balance
from databases import update_balance
from inline import select_cash_in
from layouts import pick_love_card, wb, sheet
from random import choices
from cards import cards
from fsm import AdminActions

from aiogram.types import Message, ContentType, CallbackQuery
from aiogram import Bot, Dispatcher, types
from aiogram.types.message import ContentType
from aiogram.filters import Command
from aiogram import F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)


async def starting(bot: Bot):
    await set_commands(bot)


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично! Я получил фото.')


async def get_layout(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           f'Выбери тип расклада',
                           reply_markup=select_type)
    json_str = json.dumps(message.model_dump(), default=str)
    print(json_str)


async def buy_oracle_love(message: Message, bot: Bot):
    if int(await get_user_balance(message.from_user.id)) > 80:
        await update_balance(us_id=message.from_user.id, cash=-80)
        await bot.send_message(message.from_user.id,
                               f'{pick_love_card()}')
    else:
        await bot.send_message(message.from_user.id,
                               f'У тебя недостаточно денег для оплаты(\nПополни баланс')


async def get_balance(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id,
                           f'<b>Твой баланс</b> ==<b> {await get_user_balance(message.from_user.id)} rub</b>\n<b>Твой id</b> ==<b> {message.from_user.id}</b>',
                           reply_markup=select_cash_in)
    json_str = json.dumps(message.model_dump(), default=str)
    print(json_str)


async def buy_long_uni(message: Message, bot: Bot):
    if int(await get_user_balance(message.from_user.id)) > 65:
        await update_balance(us_id=message.from_user.id, cash=-65)
        ran_cards = choices(cards, k=8)
        await bot.send_message(message.from_user.id,
                               f'{ran_cards[0]}{ran_cards[1]}{ran_cards[2]}{ran_cards[3]}{ran_cards[4]}{ran_cards[5]}{ran_cards[6]}{ran_cards[7]}')
    else:
        await bot.send_message(message.from_user.id,
                               f'У тебя недостаточно денег для оплаты(\nПополни баланс')


async def buy_triple(message: Message, bot: Bot):
    if int(await get_user_balance(message.from_user.id)) > 45:
        await update_balance(us_id=message.from_user.id, cash=-45)
        ran_cards = choices(cards, k=3)
        await bot.send_message(message.from_user.id,
                               f'<b>Прошлое</b>\n{ran_cards[0]}<b>Настоящее</b>\n{ran_cards[1]}<b>Будущее</b>\n{ran_cards[2]}')
    else:
        await bot.send_message(message.from_user.id,
                               f'У тебя недостаточно денег для оплаты(\nПополни баланс')


async def buy_short_uni(message: Message, bot: Bot):
    if int(await get_user_balance(message.from_user.id)) > 40:
        await update_balance(us_id=message.from_user.id, cash=-40)
        ran_cards = choices(cards, k=4)
        await bot.send_message(message.from_user.id,
                               f'{ran_cards[0]}{ran_cards[1]}{ran_cards[2]}{ran_cards[3]}')
    else:
        await bot.send_message(message.from_user.id,
                               f'У тебя недостаточно денег для оплаты(\nПополни баланс')


async def get_start(message: Message, bot: Bot):
    await db_table_val(user_id=message.from_user.id, user_balance=100000)
    if await get_user_admin(us_id=message.from_user.id) == 1:
        await bot.send_message(message.from_user.id,
                               f'<b>Привет, {message.from_user.first_name}!</b>\nВ этом боте ты можешь получить расклад на любую тему!',
                               reply_markup=reply_keyboard_admin)
    else:
        await bot.send_message(message.from_user.id,
                               f'<b>Привет, {message.from_user.first_name}!</b>\nВ этом боте ты можешь получить расклад на любую тему!',
                               reply_markup=reply_keyboard)


async def admin_panel(message: Message, bot: Bot):
    if await get_user_admin(us_id=message.from_user.id) == 1:
        await bot.send_message(message.from_user.id,
                               f'Админ-панель',
                               reply_markup=admin_panel_keyboard)
        json_str = json.dumps(message.model_dump(), default=str)
        print(json_str)
    else:
        await bot.send_message(message.from_user.id,
                               f'Вы не являетесь администратором!')


async def change_balance(message: Message, bot: Bot, state: FSMContext):
    balance_update_request = message.text.split(' ')
    try:
        balance_update_request = [int(i) for i in balance_update_request]
        await update_balance(us_id=balance_update_request[0], cash=balance_update_request[1])
        await bot.send_message(message.from_user.id,
                               f'Баланс пользователя {balance_update_request[0]} увеличен на {balance_update_request[1]}.')
        await state.clear()
    except Exception:
        await bot.send_message(message.from_user.id,
                               f'Вы ввели неверные данные, попробуйте еще раз.')
        await state.clear()
        await bot.send_message(message.from_user.id,
                               f'Админ-панель',
                               reply_markup=admin_panel_keyboard)
        json_str = json.dumps(message.model_dump(), default=str)
        print(json_str)


async def add_new_admin(message: Message, bot: Bot, state: FSMContext):
    try:
        await add_admin(int(message.text))
        await bot.send_message(message.from_user.id,'Пользователь назначен администратором')
    except Exception:
        await bot.send_message(message.from_user.id,
                               f'Вы ввели неверные данные, попробуйте еще раз.')
        await state.clear()
        await bot.send_message(message.from_user.id,
                               f'Админ-панель',
                               reply_markup=admin_panel_keyboard)
        json_str = json.dumps(message.model_dump(), default=str)
        print(json_str)


async def start():
    bot = Bot(token=config.BOT_TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(starting)

    dp.callback_query.register(buy_triple, F.data == 'pay_for_45')
    dp.callback_query.register(buy_oracle_love, F.data == 'pay_for_80')
    dp.callback_query.register(buy_long_uni, F.data == 'pay_for_65')
    dp.callback_query.register(buy_short_uni, F.data == 'pay_for_40')
    dp.message.register(succ_cash_in_150, F.successful_payment)
    dp.message.register(get_balance, F.text == 'Баланс')
    dp.callback_query.register(cash_in_150, F.data == 'cash_in_150r')
    dp.callback_query.register(cash_in_250, F.data == 'cash_in_250r')
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.callback_query.register(all_callback)
    dp.message.register(get_layout, F.text == 'Получить расклад')
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    dp.message.register(admin_panel, F.text == 'Админ-панель')
    dp.message.register(change_balance, StateFilter(AdminActions.change_balance))
    dp.message.register(add_new_admin, StateFilter(AdminActions.add_admin))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())

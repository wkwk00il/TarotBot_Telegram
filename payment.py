from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery, CallbackQuery
import config
from databases import update_balance


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def cash_in_150(call: CallbackQuery, bot: Bot):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Пополнение на 150р',
        description='Пополнение на 150р',
        payload='fill_in',
        provider_token=config.PAYMENTS_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Пополнение',
                amount=15000
            )
        ],
        provider_data=None,
    )

async def succ_cash_in_150(message: Message, bot: Bot):
    await update_balance(us_id=message.from_user.id, cash=150)
    msg="Поздравляем! Баланс пополнен на 150р"
    await message.answer(msg)
    
    
async def cash_in_250(call: CallbackQuery, bot: Bot):
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title='Пополнение на 250р',
        description='Пополнение на 250р',
        payload='fill_in',
        provider_token=config.PAYMENTS_TOKEN,
        currency='rub',
        prices=[
            LabeledPrice(
                label='Пополнение',
                amount=25000
            )
        ],
        provider_data=None,
    )

async def succ_cash_in_250(message: Message, bot: Bot):
    await update_balance(us_id=message.from_user.id, cash=250)
    msg="Поздравляем! Баланс пополнен на 250р"
    await message.answer(msg)
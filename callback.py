from aiogram import Bot
from aiogram.types import CallbackQuery, LabeledPrice, Message
import config
from inline import pay_for_layout_40, pay_for_layout_65, pay_for_layout_80, pay_for_layout_45


async def select_layout(call: CallbackQuery, bot: Bot):
    type = call.data
    if type == 'short_uni':
        answer = f'Ты выбрал(а) короткий универсальный расклад.\nЭтот тип расклада включает в себя 4 карты с подробными пояснениями.\nПодойдет для гадания на простые вопросы\n<b>Стоимость == 40р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_40)
        await call.answer()
    if type == 'long_uni':
        answer = f'Ты выбрал(а) длинный универсальный расклад.\nЭтот тип расклада включает в себя 8 карт с подробными пояснениями.\nПодойдет для гадания на простые вопросы\n<b>Стоимость == 70р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_65)
        await call.answer()
    if type == 'oracle_love':
        answer = f'Ты выбрал(а) расклад "Оракул любви".\nЭтот тип расклада поможет тебе разобраться в любовных отношениях с другим человеком.\nТы узнаешь: текущее положение дел, причины твоего беспокойства, отношение любимого человека и совет Оракула\n<b>Стоимость == 80р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_80)
        await call.answer()
    if type == 'triple':
        answer = f'Ты выбрал(а) триплет.\nЭтот тип расклада может использоваться для гадания на любые вопросы.\nТы узнаешь: предысторию события, суть настоящего, совет на будущее\n<b>Стоимость == 45р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_45)
        await call.answer()
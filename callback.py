from aiogram import Bot
from aiogram.types import CallbackQuery, LabeledPrice, Message
import config
from inline import pay_for_layout_40, pay_for_layout_65, pay_for_layout_80, pay_for_layout_45, admin_panel_keyboard
from aiogram.fsm.context import FSMContext
from fsm import AdminActions


async def all_callback(call: CallbackQuery, bot: Bot, state: FSMContext):
    data = call.data
    if data == 'short_uni':
        answer = f'Ты выбрал(а) короткий универсальный расклад.\nЭтот тип расклада включает в себя 4 карты с подробными пояснениями.\nПодойдет для гадания на простые вопросы\n<b>Стоимость == 40р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_40)
        await call.answer()
    if data == 'long_uni':
        answer = f'Ты выбрал(а) длинный универсальный расклад.\nЭтот тип расклада включает в себя 8 карт с подробными пояснениями.\nПодойдет для гадания на простые вопросы\n<b>Стоимость == 70р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_65)
        await call.answer()
    if data == 'oracle_love':
        answer = f'Ты выбрал(а) расклад "Оракул любви".\nЭтот тип расклада поможет тебе разобраться в любовных отношениях с другим человеком.\nТы узнаешь: текущее положение дел, причины твоего беспокойства, отношение любимого человека и совет Оракула\n<b>Стоимость == 80р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_80)
        await call.answer()
    if data == 'triple':
        answer = f'Ты выбрал(а) триплет.\nЭтот тип расклада может использоваться для гадания на любые вопросы.\nТы узнаешь: предысторию события, суть настоящего, совет на будущее\n<b>Стоимость == 45р</b>\nОплатить можешь по кнопке ниже'
        await call.message.answer(answer, reply_markup=pay_for_layout_45)
        await call.answer()
    if data == 'test111':
        await call.message.answer('sosi1')
        await call.answer()
    if data == 'change_balance':
        await call.message.answer(
            f'Введите telegram id пользователя и сумму, которую необходимо прибавить к балансу через пробел.\nПример: 0123456789 100')
        await call.answer()
        await state.set_state(AdminActions.change_balance)
    if data == 'add_admin':
        await call.message.answer(
            f'Введите telegram id пользователя, которого необходимо назначить администратором:')
        await call.answer()
        await state.set_state(AdminActions.add_admin)
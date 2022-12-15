from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from Filters import IsPrivate
from keyboards.default import kb_menu
from states import register
from loader import dp
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


@dp.message_handler(IsPrivate(), Command('register'))
async def register_(message: types.message):
    kb_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(f'{message.from_user.first_name}'),
            ],
        ],
        resize_keyboard=True
    )

    await message.answer('Привет ты начал регистрацию\n'
                         'Введи своё имя:', reply_markup=kb_menu)
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)

    data = await  state.get_data()
    name = data.get('test1')

    await message.answer(f'{name} сколько тебе лет?')
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state2(message: types.message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await  state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'Твоё имя {name}\n'
                         f'Тебе {years} лет', reply_markup=kb_menu)
    await state.finish()

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import register
from loader import dp


@dp.message_handler(Command('register'))
async def register_(message: types.message):
    await message.answer('Привет ты начал регистрацию\n'
                         'Введи своё имя:')
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
async def state1(message: types.message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await  state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f'Регистрация успешно завершена\n'
                         f'Твоё имя {name}\n'
                         f'Тебе {years} лет')
    await state.finish()
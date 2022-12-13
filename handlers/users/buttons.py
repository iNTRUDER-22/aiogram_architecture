from aiogram import types

from loader import dp

@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f'Вы написали 10 \n')

@dp.message_handler(text='11')
async def buttons_test(message: types.Message):
    await message.answer(f'Вы написали 11 \n')

@dp.message_handler(text='100')
async def buttons_test(message: types.Message):
    await message.answer(f'Вы написали 100 \n')
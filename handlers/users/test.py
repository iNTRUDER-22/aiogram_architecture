from aiogram import types
from keyboards.default import kb_test
from loader import dp

@dp.message_handler(text='Любой текст')
async def test(message: types.Message):
    await message.answer(f'Тут должен быть какой то текст', reply_markup=kb_test)
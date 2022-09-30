from aiogram import types
from loader import dp
from keyboards.default import kb_test


@dp.message_handler(text='Любой текст')
async def test(message: types.Message):
    await message.answer('тут должен быть какой-то текст', reply_markup=kb_test)

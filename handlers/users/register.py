from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup

from keyboards.default import kb_menu
from loader import dp
from states import register


@dp.message_handler(Command('register'))
async def register_(message: types.Message):
    kb = ReplyKeyboardMarkup([
        [
            message.from_user.full_name
        ]
    ], resize_keyboard=True)

    await message.answer('Привет, ты начал регистрацию!\nВведи своё имя', reply_markup=kb)
    await register.test1.set()


@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state: FSMContext):

    answer = message.text
    await state.update_data(test1=answer)
    await message.answer(f'{answer}, сколько тебе лет?', reply_markup=types.ReplyKeyboardRemove())
    await register.test2.set()


@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test2=answer)

    data = await state.get_data()
    name = data.get('test1')
    age = data.get('test2')
    await message.answer('Регистрация успешно завершена\n'
                   f'Имя: {name}\n'
                   f'Возраст: {age} лет', reply_markup=kb_menu)

    await state.finish()

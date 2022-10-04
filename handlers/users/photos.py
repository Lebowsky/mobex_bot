from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from states import Photos
from utils import get_img_url

kb_more = ReplyKeyboardMarkup([[KeyboardButton('ЕЩЁ')]], resize_keyboard=True)


@dp.message_handler(Command('photo'))
async def photos_start(message: types.Message):
    await message.answer(text='Введи текст запроса картинки. Для выхода введи "!q"')
    await Photos.get_photos.set()


@dp.message_handler(text='!q', state=Photos.get_photos)
async def photos_start(message: types.Message, state: FSMContext):
    await message.answer('Подбор картинок деактивирован.')
    await state.finish()


@dp.message_handler(text='ЕЩЁ', state=Photos.get_photos)
async def get_more(message: types.Message, state: FSMContext):
    data = await state.get_data()

    urls = data.get('urls')
    nxt = data.get('next')
    url = urls[nxt]
    nxt += 1

    if nxt == len(urls):
        await message.answer('Нет больше картинок')
        return
    try:
        await dp.bot.send_photo(chat_id=message.chat.id, photo=url, reply_markup=kb_more,
                                parse_mode=types.ParseMode.HTML)
    except Exception as ex:
        print(f'404: {url}')
    finally:
        await state.update_data({
            'urls': urls,
            'next': nxt
        })


@dp.message_handler(state=Photos.get_photos)
async def get_photos(message: types.Message, state: FSMContext):
    answer = message.text
    urls = get_img_url(answer)

    if urls:
        await state.update_data({
            'urls': urls,
            'next': 0
        })
        url = urls[0]
        try:
            await dp.bot.send_photo(chat_id=message.chat.id, photo=url, reply_markup=kb_more,
                                    parse_mode=types.ParseMode.HTML)
        except Exception:
            await message.reply(text='Попробуй еще', reply_markup=kb_more)
            print(f'404: {url}')
    else:
        await message.reply('Ничего не найдено')

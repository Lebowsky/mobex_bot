from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def get_group_id(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)

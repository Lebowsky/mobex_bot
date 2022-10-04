from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.db_gino import db

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


__all__ = ['bot', 'storage', 'dp', 'db']

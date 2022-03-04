from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from creds import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=API_TOKEN)  # os.getenv('TOKEN')
dp = Dispatcher(bot, storage=storage)

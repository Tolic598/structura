# main.py
from aiogram import executor
from bot.bot import dp
from bot.handlers import *

from bot import bot

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

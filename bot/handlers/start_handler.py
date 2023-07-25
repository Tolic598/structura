# bot/handlers/start_handler.py
from aiogram import types
from bot.bot import dp

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я твой бот. Чем могу помочь?")

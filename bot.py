import logging
import requests
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN

# Логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Привет! Напиши /usd чтобы узнать курс доллара.")

@dp.message_handler(commands=['usd'])
async def usd_cmd(message: types.Message):
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        data = response.json()
        usd = data["Valute"]["USD"]["Value"]
        await message.answer(f"💵 Курс доллара: {usd:.2f} ₽")
    except Exception as e:
        await message.answer("Ошибка при получении курса валюты 😢")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

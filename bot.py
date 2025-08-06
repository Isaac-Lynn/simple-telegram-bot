import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
from config import TOKEN

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message()
async def handle_message(message: Message):
    if message.text == "/start":
        await message.answer("Привет! Напиши /usd чтобы узнать курс доллара.")
    elif message.text == "/usd":
        try:
            response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
            data = response.json()
            usd = data["Valute"]["USD"]["Value"]
            await message.answer(f" Курс доллара: {usd:.2f} ₽")
        except Exception as e:
            await message.answer("Произошла ошибка при получении данных 😔")
    else:
        await message.answer("Я тебя не понимаю. Используй /start или /usd.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

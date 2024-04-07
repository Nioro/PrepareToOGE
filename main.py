from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import keyboard

token = "6892099382:AAFy_VsH15ooMiENXr6sKToJpxpQRCDbpLA"

bot = Bot(token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await (message.answer
        (
            f"Привет, Это телеграм-бот для подготовки к ОГЭ. Выбери интересующий тебя предмет", reply_markup=keyboard.main_kb
        )
    )

@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "математика":
        await message.answer("Выберите материал для изучения", reply_markup=keyboard.math_kb)
    if msg == "русский язык":
        await message.answer("Выберите материал для изучения", reply_markup=keyboard.russian_kb)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

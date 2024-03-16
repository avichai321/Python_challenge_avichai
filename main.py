import asyncio
import logging
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from dotenv import load_dotenv
from aiogram.filters import CommandStart

load_dotenv()

BOT_TOKEN = "6899094929:AAFETEcjLtKLdQUKpHrDD1Tk2E8KaAk9AEQ"
bot = Bot(token = (BOT_TOKEN))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}. Let's start! see the Magic")


@dp.message()
async def answer_as_message(message: types.message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except Exception:
        await message.answer("Not supported...")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())



'''if message.text == "bzat":
            await message.answer(text="why you curse me")
        elif message.text == "one piece":
            await message.answer(text="Eiichiro Oda")
        elif message.text == "naruto":
            await message.answer(text="Masashi Kishimoto")
        elif message.text == "dragon ball":
            await message.answer(text="Akira Toriyama")
        else:
            await message.answer(text="Not Recognize")'''

import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")

# Logging
logging.basicConfig(level=logging.INFO)

# Initialize bot
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton('/join'))
    await message.answer(
        f"👋 Welcome to the Komiti Game!\n"
        f"Admin: {ADMIN_USERNAME}\n"
        f"Use /join to participate in the Komiti.",
        reply_markup=keyboard
    )

# /join command
@dp.message_handler(commands=['join'])
async def join_game(message: types.Message):
    await message.answer(
        "✅ You have successfully joined this Komiti round.\nWait for the admin to start."
    )

# Unknown text handler
@dp.message_handler()
async def unknown_message(message: types.Message):
    await message.answer("❗ Please use the buttons provided.")

# Start bot polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
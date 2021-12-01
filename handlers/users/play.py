from aiogram import types

from filters import GameWord
from loader import dp


@dp.message_handler(GameWord())
async def play(message: types.Message):
    await message.answer(message.text)


@dp.message_handler()
async def unknown_word(message: types.Message):
    user_text = message.text
    await message.reply(f"Unknown word: {user_text}")

import random

from aiogram import types

from filters import GameWord
from loader import dp


@dp.message_handler(GameWord())
async def play(message: types.Message):
    game_words = ["камень", "ножницы", "бумага"]
    bot_word = random.choice(game_words)
    user_word = message.text.lower()

    await message.reply("Игра началась! \n"
                        f"Вы показали: {user_word} \n"
                        f"Бот показал: {bot_word} \n")

    if (user_word == "камень" and bot_word == "ножницы" \
            or user_word == "ножницы" and bot_word == "бумага" \
            or user_word == "бумага" and bot_word == "камень"):
        await message.answer("Вы выиграли!")
    elif user_word == bot_word:
        await message.answer("Ничья!")
    else:
        await message.answer("Вы проиграли :(")


@dp.message_handler()
async def unknown_word(message: types.Message):
    user_text = message.text
    await message.reply(f"Неизвестное слово: {user_text}")

import random

from aiogram import types

from filters import GameWord
from loader import dp


@dp.message_handler(GameWord())
async def play(message: types.Message):
    game_words = ["rock", "paper", "scissors"]
    bot_word = random.choice(game_words)
    user_word = message.text.lower()

    await message.reply("Игра началась! \n"
                        f"Вы показали: {user_word} \n"
                        f"Бот показал: {bot_word} \n")

    if (user_word == "rock" and bot_word == "scissors" \
            or user_word == "scissors" and bot_word == "paper" \
            or user_word == "paper" and bot_word == "rock"):
        await message.answer("Вы выиграли!")
    elif user_word == bot_word:
        await message.answer("Ничья!")
    else:
        await message.answer("Вы проиграли :(")


@dp.message_handler()
async def unknown_word(message: types.Message):
    user_text = message.text
    await message.reply(f"Unknown word: {user_text}")

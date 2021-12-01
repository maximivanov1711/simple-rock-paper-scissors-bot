from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("Привет, я могу сыграть с тобой в камень, ножницы, бумага. \n"
                         "Просто отправь мне одно из этих слов (камень, ножницы, бумага).")

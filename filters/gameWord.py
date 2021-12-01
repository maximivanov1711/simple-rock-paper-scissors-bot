from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class GameWord(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        game_words = ["камень", "ножницы", "бумага"]
        user_text = message.text.lower()

        return user_text in game_words

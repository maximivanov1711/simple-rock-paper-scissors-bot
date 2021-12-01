from loader import dp
from .gameWord import GameWord

if __name__ == "filters":
    dp.filters_factory.bind(GameWord)

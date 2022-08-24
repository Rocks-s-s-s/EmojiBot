from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from config import TOKEN

'''
    EmojiBot
    Может работать по двум алгоритмам:
    1. Вставляет смайлы после известной фразы.
    2. Вставляет смайлы вместо известной фразы.
'''

#TODO: 0. Обдумать как будет происходить процесс вставки смайла в текст.
#TODO: 1. Считать файлы с данными, так, чтобы удобно было потом работать.
#TODO: 2. Реализовать первый алгоритм, который вставляет после известной фразы смайл.
#TODO: 3. Добавить на каждую фразу по нескольку смайлов (пока у нас по одному на каждую).



bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
# Странная переменная, для чего этооооооооооо?
y = 0
emojifile = open('emoji', 'r')
phrasesfile = open('phrases', 'r')

emoji = [emojifile]
phrases = [phrasesfile]

@dp.message_handler()
async def get_message(message: types.Message):
    pass


if __name__ == '__main__':
    executor.start_polling(dp)
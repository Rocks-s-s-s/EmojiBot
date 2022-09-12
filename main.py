from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from config import TOKEN

#TODO: 0. +Обдумать как будет происходить процесс вставки смайла в текст.
#TODO: 1. +Считать файлы с данными, так, чтобы удобно было потом работать.
#TODO: 2. +Реализовать первый алгоритм, который вставляет после известной фразы смайл.
#TODO: 3. Добавить на каждую фразу по нескольку смайлов (пока у нас по одному на каждую).
#TODO: 4. Реализовать второй алгоритм, который заменяет фразу на смайл

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

emojifile = open('emoji.txt', 'r')
phrasesfile = open('phrases.txt', 'r')

emojifile.readlines()
phrasesfile.readlines()

emoji = []
phrases = []

for line in phrasesfile:
    phrases.append(line.split('#'))
for line in emojifile:
    emoji.append(line.split('#'))
@dp.message_handler()
async def get_message(message: types.Message):
    line = 0
    for phrase in phrases:
        for p in phrase:
            pos=message.find(p)
            if pos > -1:
                pos = pos + len(p)
                message = message[:pos]+emoji[line] + message[pos+1:]
        line = line + 1


if __name__ == '__main__':
    executor.start_polling(dp)
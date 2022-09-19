import random

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from config import TOKEN

# TODO: 0. +Обдумать как будет происходить процесс вставки смайла в текст.
# TODO: 1. +Считать файлы с данными, так, чтобы удобно было потом работать.
# TODO: 2. +Реализовать первый алгоритм, который вставляет после известной фразы смайл.
# TODO: 3. Добавить на каждую фразу по нескольку смайлов (пока у нас по одному на каждую).
# TODO: 4. Реализовать второй алгоритм, который заменяет фразу на смайл

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
typeKeyboard = types.InlineKeyboardMarkup()
type1Button = types.InlineKeyboardButton(text='type 1', callback_data='type1Button_click')
type2Button = types.InlineKeyboardButton(text='type 2', callback_data='type2Button_click')
typeKeyboard.add(type1Button, type2Button)

emojifile = open('emoji.txt', 'r')
phrasesfile = open('phrases.txt', 'r')

emoji = []
phrases = []

for line in phrasesfile:
    phrases.append(line.strip().split('#'))
for line in emojifile:
    emoji.append(line.strip().split('#'))


def emojizeText1(text):
    line = 0
    for phrase in phrases:
        for p in phrase:
            pos = text.find(p)
            if pos > -1:
                pos = pos + len(p)
                text = text[:pos] + random.choice(emoji[line]) + text[pos + 1:]
        line = line + 1
    return emojize(text)


def emojizeText2(text):
    line = 0
    for phrase in phrases:
        for p in phrase:
            pos = text.find(p)
            if pos > -1:
                text = text[:pos] + random.choice(emoji[line]) + text[pos + len(p):]
        line = line + 1
    return emojize(text)


@dp.message_handler()
async def get_message(message: types.Message):
    await message.answer('Выберите тип', reply_markup=typeKeyboard)
@dp.callback_query_handler(text='type1Button_click')
async def type1Button_click(call: types.CallbackQuery):
    await call.message.answer(emojizeText1(call.message.text))

@dp.callback_query_handler(text='type2Button_click')
async def type2Button_click(call: types.CallbackQuery):
    await call.message.answer(emojizeText2(call.message.text))

if __name__ == '__main__':
    executor.start_polling(dp)

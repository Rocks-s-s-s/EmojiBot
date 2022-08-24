import dp as dp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
y = 0
emojifile = open('emoji','r')
phrasesfile = open('phrases','r')

emoji = [emojifile]
phrases = [phrasesfile]

@dp.message_handler()
async def get_message(message: types.Message):










if __name__ == '__main__':
    executor.start_polling(dp)
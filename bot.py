import os
import logging

from logging.handlers import RotatingFileHandler
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')


log_file = 'bot.log'
file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=2)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger('').addHandler(file_handler)

translit_dict = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA',
    'Ь': '',    
}

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Hello, {user_name} отправь ФИО для форматирования!"
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)
@dp.message_handler()
async def send_echo(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = ''.join(translit_dict.get(char, char) for char in message.text.upper())
    logging.info(f"{user_name=} {user_id=} sent message: {text}")
    await bot.send_message(user_id, text)
    
if __name__ == '__main__':
    logging.info("Bot is starting...")
    executor.start_polling(dp)
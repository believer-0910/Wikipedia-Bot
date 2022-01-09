import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5072639859:AAFhYOHW6IQlPE55vqG7Yw2wwMTxB878dW0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(
        "Hi!\nI'm Wikipedia bot!\n"
        "I will help you find information from wikipedia.\n"
        "Please send me topic and I will find information about the you sent me.")


@dp.message_handler()
async def wikipediaBot(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except: await message.answer("This topic is not found. Sorry.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

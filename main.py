from aiogram import Bot, Dispatcher, executor,types
from config import Token_AIP
import asyncio
import logging
#*********************************************************************#

bot =Bot(Token_AIP)
dp = Dispatcher(bot)

#*********************************************************************#

@dp.message_handler(commands=['start']) #start bot command
async def start_command(message: types.Message):    
    await message.answer("Hello! I am your bot. How can I assist you today?")

@dp.message_handler(commands=['help']) #help command
async def help_command(message: types.Message):
    await message.answer("Here are the commands you can use:\n/start - Start the bot\n/help - Get help information")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")
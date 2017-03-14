import os
import logging
from telegram.ext import (Updater, CommandHandler)

#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(bot, update):
    updater = os.getenv("BOTOKEN")
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

if __name__ == "__main__":
    start()

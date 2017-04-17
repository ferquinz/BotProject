import os
import logging

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

#https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start_cmd_handler(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    bot.sendMessage(chat_id=update.message.chat_id, text=str(update))

def text_handler_f(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)


def main():
    updater = Updater(os.getenv("BOTOKEN"))
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start_cmd_handler)
    text_handler = MessageHandler(Filters.text, text_handler_f)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()

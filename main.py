import os
import telebot
from dotenv import load_dotenv
from appearance import register_handlers

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

def log_start(func):
    def wrapper():
        print("Бот запущено!")
        func()
    return wrapper

@log_start
def main():
    register_handlers(bot) 
    bot.polling()

if __name__ == "__main__":
    main()

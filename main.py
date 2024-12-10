import telebot
from appearance import register_handlers
from deco import log_start
from get_token import get_token


@log_start
def main():
    API_TOKEN = get_token()
    bot = telebot.TeleBot(API_TOKEN)
    register_handlers(bot) 
    bot.polling()


if __name__ == "__main__":
    main()

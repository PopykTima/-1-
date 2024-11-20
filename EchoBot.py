import telebot

API_TOKEN = '7674474171:AAF71ghIszAa0cH_ZwBVz0PLsS-nt0EV81s'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=[ 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()  

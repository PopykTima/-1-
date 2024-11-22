import telebot
import random
from datetime import datetime

TOKEN = "7798938615:AAFGExwsrhnYYj2VPyFjtlroFx8hJKZk5vQ"
bot = telebot.TeleBot(TOKEN)

ANEKDOTS_FILE = "anekdots.txt"
last_sent = {}

try:
    with open(ANEKDOTS_FILE, "r", encoding="utf-8") as file:
        anekdots = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    anekdots = ["Анекдотів поки немає 😔"]

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        telebot.types.InlineKeyboardButton("Отримати анекдот", callback_data="get_anekdot"),
        telebot.types.InlineKeyboardButton("Не хочу анекдот", callback_data="dont_want_anekdot")
    )
    bot.send_message(
        message.chat.id,
        f"Привіт, {message.from_user.first_name}! Обери опцію:",
        reply_markup=keyboard,
    )

def send_anekdot(chat_id, user_id):
    now = datetime.now()
    if last_sent.get(user_id, datetime.min).date() != now.date():
        last_sent[user_id] = now
        bot.send_message(chat_id, random.choice(anekdots))
    else:
        bot.send_message(chat_id, "Сьогодні ви вже отримали анекдот! Спробуйте завтра 😊")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "get_anekdot":
        send_anekdot(call.message.chat.id, call.from_user.id)
    elif call.data == "dont_want_anekdot":
        bot.send_message(call.message.chat.id, "Ну то виходь з відси ДУШНІЛА! 😌")

@bot.message_handler(commands=['anekdot'])
def anekdot_command(message):
    send_anekdot(message.chat.id, message.from_user.id)

if __name__ == "__main__":
     print("Бот запущено!")
     bot.polling()

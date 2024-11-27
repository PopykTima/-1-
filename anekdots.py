import random
from datetime import datetime

ANEKDOTS_FILE = "anekdots.txt"
last_sent = {}

try:
    with open(ANEKDOTS_FILE, "r", encoding="utf-8") as file:
        anekdots = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    anekdots = ["Анекдотів поки немає 😔"]

def send_anekdot(bot, chat_id, user_id):
    now = datetime.now()
    if last_sent.get(user_id, datetime.min).date() != now.date():
        last_sent[user_id] = now
        bot.send_message(chat_id, random.choice(anekdots))
    else:
        bot.send_message(chat_id, "Сьогодні ви вже отримали анекдот! Спробуйте завтра 😊")

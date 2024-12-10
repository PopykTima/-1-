from telebot import types
import telebot 
from anekdots import send_anekdot

def register_handlers(bot):
    
    @bot.message_handler(commands=['start'])
    def start(message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("Отримати анекдот", callback_data="get_anekdot"),
            types.InlineKeyboardButton("Не хочу анекдот", callback_data="dont_want_anekdot")
        )
        bot.send_message(
            message.chat.id,
            f"Привіт, {message.from_user.first_name}! Обери опцію:",
            reply_markup=keyboard,
        )

    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        if call.data == "get_anekdot":
            send_anekdot(bot, call.message.chat.id, call.from_user.id)
        elif call.data == "dont_want_anekdot":
            bot.send_message(call.message.chat.id, "Ну то виходь з відси ДУШНІЛА! 😌")

    @bot.message_handler(commands=['anekdot'])
    def anekdot_command(message):
        send_anekdot(bot, message.chat.id, message.from_user.id)

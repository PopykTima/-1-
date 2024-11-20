import logging
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

ANEKDOTS_FILE = "anekdots.txt"

last_sent = {}

def load_anekdots(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        logging.error("Файл з анекдотами не знайдено!")
        return ["Анекдотів поки немає 😔"]

anekdots = load_anekdots(ANEKDOTS_FILE)

async def start(update: Update, context: CallbackContext) -> None:
    buttons = [
        [InlineKeyboardButton("Отримати анекдот", callback_data="get_anekdot")],
        [InlineKeyboardButton("Я не хочу отримувати анекдот", callback_data="dont_want_anekdot")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        f"Привіт, {update.effective_user.first_name}! "
        f"Виберіть одну з опцій нижче:",
        reply_markup=reply_markup,
    )

def get_random_anekdot() -> str:
    return random.choice(anekdots)

def can_receive_anekdot(user_id: int) -> bool:
    now = datetime.now()
    if user_id in last_sent:
        last_time = last_sent[user_id]
        return last_time.date() != now.date()
    return True

async def send_anekdot(update: Update, context: CallbackContext, via_command=False) -> None:
    user_id = update.effective_user.id

    if can_receive_anekdot(user_id):
        last_sent[user_id] = datetime.now()

        anekdot = get_random_anekdot()
        if via_command:
            await update.message.reply_text(anekdot)
        else:
            await update.callback_query.answer()  
            await update.callback_query.message.reply_text(anekdot)
    else:
        message = "Ви вже отримали свій анекдот сьогодні! Спробуйте завтра 😊"
        if via_command:
            await update.message.reply_text(message)
        else:
            await update.callback_query.answer()  
            await update.callback_query.message.reply_text(message)

async def dont_want_anekdot(update: Update, context: CallbackContext) -> None:
    await update.callback_query.answer()  
    await update.callback_query.message.reply_text("Ну то виходь з відци ДУШНІЛА! 😌")

async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == "get_anekdot":
        await send_anekdot(update, context)
    elif query.data == "dont_want_anekdot":
        await dont_want_anekdot(update, context)

async def anekdot_command(update: Update, context: CallbackContext) -> None:
    await send_anekdot(update, context, via_command=True)

def main():
    TOKEN = "7798938615:AAFGExwsrhnYYj2VPyFjtlroFx8hJKZk5vQ"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("anekdot", anekdot_command))
    application.add_handler(CallbackQueryHandler(button_handler))  

    application.run_polling()

if __name__ == "__main__":
    main()
    

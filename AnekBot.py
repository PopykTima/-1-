import logging
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Шлях до файлу з анекдотами
ANEKDOTS_FILE = "anekdots.txt"

# Словник для збереження останніх анекдотів
last_sent = {}

# Функція для завантаження анекдотів із файлу
def load_anekdots(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        logging.error("Файл з анекдотами не знайдено!")
        return ["Анекдотів поки немає 😔"]

# Завантажуємо анекдоти при старті
anekdots = load_anekdots(ANEKDOTS_FILE)

# Команда /start
async def start(update: Update, context: CallbackContext) -> None:
    # Створюємо кнопки
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

# Функція для вибору випадкового анекдоту
def get_random_anekdot() -> str:
    return random.choice(anekdots)

# Функція для перевірки обмеження на анекдот
def can_receive_anekdot(user_id: int) -> bool:
    now = datetime.now()
    if user_id in last_sent:
        last_time = last_sent[user_id]
        # Перевіряємо, чи дата останнього анекдоту співпадає з поточною
        return last_time.date() != now.date()
    return True

# Функція для надсилання анекдоту
async def send_anekdot(update: Update, context: CallbackContext, via_command=False) -> None:
    user_id = update.effective_user.id

    # Перевіряємо, чи може користувач отримати анекдот сьогодні
    if can_receive_anekdot(user_id):
        # Зберігаємо поточний час і анекдот
        last_sent[user_id] = datetime.now()

        # Відправляємо випадковий анекдот
        anekdot = get_random_anekdot()
        if via_command:
            await update.message.reply_text(anekdot)
        else:
            await update.callback_query.answer()  # Закриваємо спінер
            await update.callback_query.message.reply_text(anekdot)
    else:
        # Якщо анекдот вже отримували сьогодні
        message = "Ви вже отримали свій анекдот сьогодні! Спробуйте завтра 😊"
        if via_command:
            await update.message.reply_text(message)
        else:
            await update.callback_query.answer()  # Закриваємо спінер
            await update.callback_query.message.reply_text(message)

# Функція для відповіді на кнопку "Я не хочу отримувати анекдот"
async def dont_want_anekdot(update: Update, context: CallbackContext) -> None:
    await update.callback_query.answer()  # Закриваємо спінер
    await update.callback_query.message.reply_text("Ну то виходь з відци ДУШНІЛА! 😌")

# Обробка кнопок
async def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    if query.data == "get_anekdot":
        await send_anekdot(update, context)
    elif query.data == "dont_want_anekdot":
        await dont_want_anekdot(update, context)

# Команда /anekdot
async def anekdot_command(update: Update, context: CallbackContext) -> None:
    await send_anekdot(update, context, via_command=True)

# Основна функція
def main():
    # Вставте ваш токен Telegram-бота
    TOKEN = "7798938615:AAFGExwsrhnYYj2VPyFjtlroFx8hJKZk5vQ"

    # Ініціалізація бота
    application = Application.builder().token(TOKEN).build()

    # Додаємо обробники команд і кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("anekdot", anekdot_command))
    application.add_handler(CallbackQueryHandler(button_handler))  # Для обробки кнопок

    # Запускаємо бота
    application.run_polling()

if __name__ == "__main__":
    main()
    

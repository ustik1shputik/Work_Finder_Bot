import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Токен бота (замените на ваш)
BOT_TOKEN = "8441485840:AAGl5YPC_g4NrsaW8U4lmPN_NuY8V2ZjZdQ"

# URL вашего Mini App (замените на реальный)
MINI_APP_URL = "https://example.com/mini-app"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start с кнопкой для открытия Mini App"""
    keyboard = [
        [InlineKeyboardButton("🔍 Найти работу", web_app=WebAppInfo(url=MINI_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Добро пожаловать в бот для поиска работы!\n\n"
        "Я помогу вам найти подходящие вакансии через наше мини-приложение.\n"
        "Нажмите кнопку ниже, чтобы начать поиск!",
        reply_markup=reply_markup
    )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /info"""
    await update.message.reply_text(
        "ℹ️ *Информация о боте:*\n\n"
        "Этот бот предназначен для поиска работы через интеграцию с Telegram Mini App.\n"
        "Основные функции:\n"
        "• Поиск вакансий\n"
        "• Фильтрация по категориям\n"
        "• Прямой контакт с работодателями\n\n"
        "Для начала работы нажмите /start",
        parse_mode="Markdown"
    )


async def post_init(application: Application) -> None:
    """Функция отправки сообщения при запуске бота"""
    await application.bot.set_my_commands([
        ("start", "Запустить бота"),
        ("info", "Информация о боте")
    ])


def main() -> None:
    # Создаем приложение и передаем токен
    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("info", info))

    # Запускаем бота
    application.run_polling()
    print("Бот запущен...")


if __name__ == "__main__":
    main()
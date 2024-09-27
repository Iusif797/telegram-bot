import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler

# Получаем токен бота из переменных окружения
TOKEN = os.getenv('7008997408:AAGn4ug4q4ok9rFDXguPqnqgjqR1-deZyjI')

# URL вашего веб-приложения (Web App)
WEB_APP_URL = 'https://telegram-expense-tracker.vercel.app/'  # Ваша ссылка на мини-приложение

async def start(update: Update, context):
    # Создаем кнопку для открытия Web App прямо в Telegram
    keyboard = [
        [InlineKeyboardButton(text="🚀 Открыть трекер расходов", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем приветственное сообщение с кнопкой для открытия Web App
    await update.message.reply_text(
        '👋 Привет! Я бот для отслеживания ваших доходов и расходов.\n\n'
        '💼 Для начала работы откройте трекер, нажав на кнопку ниже.',
        reply_markup=reply_markup
    )

async def help_command(update: Update, context):
    await update.message.reply_text(
        '📝 Команды:\n'
        '/start - Начать работу с ботом и открыть трекер\n'
        '/help - Показать список доступных команд'
    )

def main():
    # Создаем объект Application и передаем ему токен вашего бота
    application = Application.builder().token(TOKEN).build()

    # Определяем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()

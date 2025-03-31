from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7801901248:AAGTt0tpjDeKogSTVrKRnxASBMnTgarPnTs"
WEB_APP_URL = "https://e8f4d75111005f2c119a3cb3f4cad7e5.serveo.net"

print("Запускаю бота...")  # Проверка 1

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Получил /start!")  # Проверка 2
    keyboard = [[InlineKeyboardButton("Читать", web_app=WebAppInfo(url=WEB_APP_URL))]]
    await update.message.reply_text("Привет! Жми читать!", reply_markup=InlineKeyboardMarkup(keyboard))
    print("Отправил ответ!")  # Проверка 3

print("Создаю приложение...")  # Проверка 4
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Стартую бота...")  # Проверка 5
app.run_polling()
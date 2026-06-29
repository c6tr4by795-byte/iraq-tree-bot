from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8633332339:AAFaw4eQ09genK4d5luEoTgieGYzvmnoagk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌳 أهلاً بك في مشروع الزراعة")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()

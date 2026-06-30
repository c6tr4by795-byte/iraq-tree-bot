from telegram import Update
from telegram.ext import ContextTypes


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 أي رسالة وصلتني")

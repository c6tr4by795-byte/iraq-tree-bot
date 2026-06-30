from telegram import Update
from telegram.ext import ContextTypes


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if ":" not in text:
        return

    await update.message.reply_text(
        f"""✅ وصلت الدالة بنجاح

📋 البيانات التي استلمتها:

{text}
"""
    )

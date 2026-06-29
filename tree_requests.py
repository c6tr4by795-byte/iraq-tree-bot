from telegram import Update
from telegram.ext import ContextTypes


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if ":" not in text:
        return

    await update.message.reply_text(
        f"""✅ تم استلام طلب الشتلة بنجاح.

📋 البيانات:

{text}

⏳ سيتم إرسال طلبك إلى المشرف للمراجعة.
"""
    )

from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if ":" not in text:
        return

    # رسالة للمشرف
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""📥 طلب شتلة جديد

👤 المستخدم:
{update.effective_user.full_name}

🆔 ID:
{update.effective_user.id}

📋 البيانات:

{text}
"""
    )

    # رسالة للمستخدم
    await update.message.reply_text(
        "✅ تم إرسال طلبك إلى المشرف.\n\nسيتم التواصل معك بعد مراجعة الطلب."
    )

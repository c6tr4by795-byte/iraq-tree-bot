from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID

users = {}


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in users:
        users[user_id] = {}

    data = users[user_id]

    if "name" not in data:
        data["name"] = text
        await update.message.reply_text("📱 أرسل رقم الهاتف:")
        return

    if "phone" not in data:
        data["phone"] = text
        await update.message.reply_text("🏙️ أرسل المحافظة:")
        return

    if "city" not in data:
        data["city"] = text
        await update.message.reply_text("📍 أرسل القضاء:")
        return

    if "district" not in data:
        data["district"] = text
        await update.message.reply_text("📌 أرسل المنطقة:")
        return

    if "area" not in data:
        data["area"] = text
        await update.message.reply_text("🌱 كم شتلة تريد؟")
        return

    if "count" not in data:
        data["count"] = text

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"""
📥 طلب شتلة جديد

👤 الاسم: {data['name']}
📱 الهاتف: {data['phone']}
🏙️ المحافظة: {data['city']}
📍 القضاء: {data['district']}
📌 المنطقة: {data['area']}
🌱 العدد: {data['count']}

🆔 User ID: {user_id}
"""
        )

        await update.message.reply_text(
            "✅ تم إرسال طلبك إلى المشرف بنجاح."
        )

        del users[user_id]

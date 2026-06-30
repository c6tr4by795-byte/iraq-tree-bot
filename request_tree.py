from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID
from admin import admin_keyboard

users = {}


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if "step" not in context.user_data:
        return

    if user_id not in users:
        users[user_id] = {}

    data = users[user_id]

    if context.user_data["step"] == "name":
        data["name"] = text
        context.user_data["step"] = "phone"
        await update.message.reply_text("📱 اكتب رقم الهاتف:")
        return

    if context.user_data["step"] == "phone":
        data["phone"] = text
        context.user_data["step"] = "province"
        await update.message.reply_text("🏙️ اكتب المحافظة:")
        return

    if context.user_data["step"] == "province":
        data["province"] = text
        context.user_data["step"] = "district"
        await update.message.reply_text("📍 اكتب القضاء:")
        return

    if context.user_data["step"] == "district":
        data["district"] = text
        context.user_data["step"] = "area"
        await update.message.reply_text("📌 اكتب المنطقة:")
        return

    if context.user_data["step"] == "area":
        data["area"] = text
        context.user_data["step"] = "count"
        await update.message.reply_text("🌱 كم شتلة تريد؟")
        return

    if context.user_data["step"] == "count":
        data["count"] = text

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"""📥 طلب شتلة جديد

👤 الاسم: {data['name']}
📱 الهاتف: {data['phone']}
🏙️ المحافظة: {data['province']}
📍 القضاء: {data['district']}
📌 المنطقة: {data['area']}
🌱 العدد: {data['count']}
""",
            reply_markup=admin_keyboard(user_id)
        )

        await update.message.reply_text(
            "✅ تم إرسال طلبك إلى المشرف."
        )

        del users[user_id]
        del context.user_data["step"]

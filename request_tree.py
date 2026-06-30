from telegram import Update
from telegram.ext import ContextTypes

from database import add_request
from config import ADMIN_ID
from admin import admin_keyboard

users = {}


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if "step" not in context.user_data:
        return

    user_id = update.effective_user.id
    text = update.message.text

    if user_id not in users:
        users[user_id] = {}

    data = users[user_id]

    # الاسم
    if context.user_data["step"] == "name":
        data["name"] = text
        context.user_data["step"] = "phone"

        await update.message.reply_text(
            "📱 اكتب رقم الهاتف:"
        )
        return

    # الهاتف
    if context.user_data["step"] == "phone":
        data["phone"] = text
        context.user_data["step"] = "province"

        await update.message.reply_text(
            "🏙️ اكتب المحافظة:"
        )
        return

    # المحافظة
    if context.user_data["step"] == "province":
        data["province"] = text
        context.user_data["step"] = "district"

        await update.message.reply_text(
            "📍 اكتب القضاء:"
        )
        return

    # القضاء
    if context.user_data["step"] == "district":
        data["district"] = text
        context.user_data["step"] = "area"

        await update.message.reply_text(
            "📌 اكتب المنطقة:"
        )
        return

    # المنطقة
    if context.user_data["step"] == "area":
        data["area"] = text
        context.user_data["step"] = "count"

        await update.message.reply_text(
            "🌱 كم شتلة تريد؟"
        )
        return

    # العدد
    if context.user_data["step"] == "count":

        data["count"] = text

        request_id = add_request(
            user_id,
            data["name"],
            data["phone"],
            data["province"],
            data["district"],
            data["area"],
            data["count"],
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"""📥 طلب شتلة جديد

🆔 رقم الطلب: {request_id}

👤 الاسم:
{data["name"]}

📱 الهاتف:
{data["phone"]}

🏙️ المحافظة:
{data["province"]}

📍 القضاء:
{data["district"]}

📌 المنطقة:
{data["area"]}

🌱 العدد:
{data["count"]}
""",
            reply_markup=admin_keyboard(request_id)
        )

        await update.message.reply_text(
            "✅ تم إرسال طلبك إلى المشرف.\n\nسيتم إشعارك بعد مراجعة الطلب."
        )

        users.pop(user_id, None)
        context.user_data.clear()

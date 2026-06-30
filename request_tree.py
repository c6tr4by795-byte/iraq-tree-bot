from telegram import Update
from telegram.ext import ContextTypes

users = {}


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if "step" not in context.user_data:
        return

    if user_id not in users:
        users[user_id] = {}

    # الاسم
    if context.user_data["step"] == "name":
        users[user_id]["name"] = text
        context.user_data["step"] = "phone"

        await update.message.reply_text(
            "📱 اكتب رقم الهاتف:"
        )
        return

    # الهاتف
    if context.user_data["step"] == "phone":
        users[user_id]["phone"] = text
        context.user_data["step"] = "province"

        await update.message.reply_text(
            "🏙️ اكتب المحافظة:"
        )
        return

    # المحافظة
    if context.user_data["step"] == "province":
        users[user_id]["province"] = text
        context.user_data["step"] = "district"

        await update.message.reply_text(
            "📍 اكتب القضاء:"
        )
        return

    # القضاء
    if context.user_data["step"] == "district":
        users[user_id]["district"] = text
        context.user_data["step"] = "area"

        await update.message.reply_text(
            "📌 اكتب المنطقة:"
        )
        return

    # المنطقة
    if context.user_data["step"] == "area":
        users[user_id]["area"] = text
        context.user_data["step"] = "count"

        await update.message.reply_text(
            "🌱 كم شتلة تريد؟"
        )
        return

    # العدد
    if context.user_data["step"] == "count":
        users[user_id]["count"] = text

        await update.message.reply_text(
            "✅ تم استلام طلبك وسيتم إرساله إلى المشرف."
        )

        del context.user_data["step"]

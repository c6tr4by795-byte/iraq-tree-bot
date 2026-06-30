from telegram import Update
from telegram.ext import ContextTypes

from request_tree import users


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("approve_"):
        user_id = int(data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text="✅ تمت الموافقة على طلبك.\n\nسيتم التواصل معك قريباً لاستلام الشتلة."
        )

        await query.edit_message_text(
            "✅ تمت الموافقة على الطلب."
        )

    elif data.startswith("reject_"):
        user_id = int(data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text="❌ تم رفض طلبك."
        )

        await query.edit_message_text(
            "❌ تم رفض الطلب."
        )

from telegram import Update
from telegram.ext import ContextTypes

from qr import create_qr


tree_number = 1


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global tree_number

    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("approve_"):

        user_id = int(data.split("_")[1])

        tree_id = f"IRQ-{tree_number:06d}"
        tree_number += 1

        qr = create_qr(tree_id)

        await context.bot.send_photo(
            chat_id=user_id,
            photo=qr,
            caption=f"""🎉 تمت الموافقة على طلبك.

🌳 رقم الشتلة:
{tree_id}

📦 هذا هو QR الخاص بالشتلة.

سيتم إعلامك بموقع وموعد الاستلام قريباً.
"""
        )

        await query.edit_message_text(
            f"✅ تمت الموافقة.\n\nرقم الشتلة: {tree_id}"
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

from telegram import Update
from telegram.ext import ContextTypes

from qr import create_qr
from database import (
    get_request,
    approve_request,
    reject_request,
)
from config import TREE_PREFIX


async def admin_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    data = query.data

    # موافقة
    if data.startswith("approve:"):

        request_id = int(data.split(":")[1])

        request = get_request(request_id)

        if not request:
            await query.edit_message_text("❌ الطلب غير موجود.")
            return

        telegram_id = request[1]

        tree_code = f"{TREE_PREFIX}-{request_id:06d}"

        approve_request(request_id, tree_code)

        qr = create_qr(tree_code)

        await context.bot.send_photo(
            chat_id=telegram_id,
            photo=qr,
            caption=f"""🎉 تمت الموافقة على طلبك

🌳 رقم الشتلة:
{tree_code}

📦 هذا هو QR الخاص بك.

سيتم إرسال موقع وموعد الاستلام قريباً.
"""
        )

        await query.edit_message_text(
            f"✅ تمت الموافقة على الطلب\n\n🌳 {tree_code}"
        )

    # رفض
    elif data.startswith("reject:"):

        request_id = int(data.split(":")[1])

        request = get_request(request_id)

        if not request:
            await query.edit_message_text("❌ الطلب غير موجود.")
            return

        telegram_id = request[1]

        reject_request(request_id)

        await context.bot.send_message(
            chat_id=telegram_id,
            text="❌ تم رفض طلبك."
        )

        await query.edit_message_text(
            "❌ تم رفض الطلب."
        )

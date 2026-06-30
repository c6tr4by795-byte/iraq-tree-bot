from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_keyboard
from database import get_tree


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # فتح البوت عن طريق QR
    if context.args:

        tree_code = context.args[0]

        tree = get_tree(tree_code)

        if tree:

            await update.message.reply_text(
                f"""🌳 معلومات الشجرة

🆔 رقم الشجرة:
{tree[9]}

👤 صاحب الشتلة:
{tree[2]}

🏙️ المحافظة:
{tree[4]}

📍 القضاء:
{tree[5]}

📌 المنطقة:
{tree[6]}

🌱 عدد الشتلات:
{tree[7]}

📋 الحالة:
{tree[8]}

📅 تاريخ الطلب:
{tree[13]}
"""
            )

        else:

            await update.message.reply_text(
                "❌ هذه الشجرة غير موجودة."
            )

        return

    context.user_data.clear()

    await update.message.reply_text(
        """🌳 أهلاً بك في مشروع شجرة العراق

ساهم بزراعة العراق... اطلب شتلتك الآن.""",
        reply_markup=main_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "request_tree":

        context.user_data.clear()
        context.user_data["step"] = "name"

        await query.message.reply_text(
            "👤 اكتب اسمك الكامل:"
        )

    elif query.data == "profile":
        await query.edit_message_text(
            "👤 حسابي",
            reply_markup=main_keyboard()
        )

    elif query.data == "map":
        await query.edit_message_text(
            "🗺️ قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "leaders":
        await query.edit_message_text(
            "🏆 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "rewards":
        await query.edit_message_text(
            "🎁 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "stats":
        await query.edit_message_text(
            "📊 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "volunteer":
        await query.edit_message_text(
            "🤝 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "partners":
        await query.edit_message_text(
            "🏢 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "news":
        await query.edit_message_text(
            "📢 قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "about":
        await query.edit_message_text(
            "🌳 مشروع شجرة العراق",
            reply_markup=main_keyboard()
        )

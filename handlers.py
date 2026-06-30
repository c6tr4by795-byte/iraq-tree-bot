from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # إذا فتح البوت عن طريق QR
    if context.args:

        tree_code = context.args[0]

        await update.message.reply_text(
            f"""🌳 معلومات الشجرة

🆔 رقم الشجرة:
{tree_code}

⏳ جاري تحميل بيانات الشجرة...
"""
        )

        return

    # البداية العادية
    context.user_data.clear()

    await update.message.reply_text(
        """🌳 أهلاً بك في مشروع شجرة العراق

ساهم في زيادة المساحات الخضراء واطلب شتلتك الآن.""",
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
            "🗺️ الخريطة قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "leaders":
        await query.edit_message_text(
            "🏆 المتصدرون قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "rewards":
        await query.edit_message_text(
            "🎁 المكافآت قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "stats":
        await query.edit_message_text(
            "📊 الإحصائيات قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "volunteer":
        await query.edit_message_text(
            "🤝 التطوع قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "partners":
        await query.edit_message_text(
            "🏢 الشركاء قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "news":
        await query.edit_message_text(
            "📢 الأخبار قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ الإعدادات قريباً",
            reply_markup=main_keyboard()
        )

    elif query.data == "about":
        await query.edit_message_text(
            "🌳 مشروع شجرة العراق",
            reply_markup=main_keyboard()
        )

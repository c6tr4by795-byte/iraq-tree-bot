from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()

    await update.message.reply_text(
        "🌳 أهلاً بك في مشروع شجرة العراق\n\n"
        "ساهم في زيادة المساحات الخضراء واطلب شتلتك الآن.",
        reply_markup=main_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "request_tree":

        context.user_data.clear()
        context.user_data["step"] = "name"

        await query.message.reply_text(
            "🌱 طلب شتلة\n\n"
            "👤 اكتب اسمك الكامل:"
        )

    elif query.data == "profile":
        await query.edit_message_text(
            "👤 حسابك\n\n"
            "🌳 عدد الأشجار: 0\n"
            "⭐ النقاط: 0",
            reply_markup=main_keyboard()
        )

    elif query.data == "map":
        await query.edit_message_text(
            "🗺️ قريباً سيتم إطلاق خريطة الأشجار.",
            reply_markup=main_keyboard()
        )

    elif query.data == "leaders":
        await query.edit_message_text(
            "🏆 لوحة المتصدرين قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "rewards":
        await query.edit_message_text(
            "🎁 نظام المكافآت قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "stats":
        await query.edit_message_text(
            "📊 الإحصائيات قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "volunteer":
        await query.edit_message_text(
            "🤝 التسجيل كمتطوع قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "partners":
        await query.edit_message_text(
            "🏢 شركاء المشروع قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "news":
        await query.edit_message_text(
            "📢 آخر أخبار المشروع قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ الإعدادات قريباً.",
            reply_markup=main_keyboard()
        )

    elif query.data == "about":
        await query.edit_message_text(
            "🌳 مشروع شجرة العراق\n\n"
            "مشروع يهدف إلى زيادة المساحات الخضراء في العراق.",
            reply_markup=main_keyboard()
        )

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import ContextTypes

from keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌳 أهلاً بك في مشروع شجرة العراق\n\nاختر الخدمة التي تريدها:",
        reply_markup=main_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plant":

        keyboard = ReplyKeyboardMarkup(
            [
                [
                    KeyboardButton(
                        "📍 إرسال موقعي",
                        request_location=True
                    )
                ]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )

        await query.message.reply_text(
            "🌱 لإضافة شجرة جديدة\n\nاضغط الزر بالأسفل لإرسال موقعك.",
            reply_markup=keyboard
        )

    elif query.data == "request_tree":
        await query.edit_message_text(
            """🌱 طلب شتلة

يرجى إرسال المعلومات التالية:

• الاسم الكامل
• رقم الهاتف
• المحافظة
• القضاء
• المنطقة
• عدد الشتلات

مثال:

الاسم: أحمد علي
الهاتف: 07XXXXXXXXX
المحافظة: النجف
القضاء: النجف
المنطقة: حي الأمير
العدد: 3
""",
            reply_markup=main_keyboard()
        )

    elif query.data == "map":
        await query.edit_message_text(
            "🗺️ قريباً ستظهر الخريطة.",
            reply_markup=main_keyboard()
        )

    elif query.data == "profile":
        await query.edit_message_text(
            "👤 حسابك\n\n🌳 الأشجار: 0\n⭐ النقاط: 0",
            reply_markup=main_keyboard()
        )

    elif query.data == "leaders":
        await query.edit_message_text(
            "🏆 لوحة المتصدرين",
            reply_markup=main_keyboard()
        )

    elif query.data == "rewards":
        await query.edit_message_text(
            "🎁 المكافآت",
            reply_markup=main_keyboard()
        )

    elif query.data == "stats":
        await query.edit_message_text(
            "📊 الإحصائيات",
            reply_markup=main_keyboard()
        )

    elif query.data == "volunteer":
        await query.edit_message_text(
            "🤝 التطوع",
            reply_markup=main_keyboard()
        )

    elif query.data == "partners":
        await query.edit_message_text(
            "🏢 الشركاء",
            reply_markup=main_keyboard()
        )    elif query.data == "news":
        await query.edit_message_text(
            "📢 الأخبار",
            reply_markup=main_keyboard()
        )

    elif query.data == "settings":
        await query.edit_message_text(
            "⚙️ الإعدادات",
            reply_markup=main_keyboard()
        )

    elif query.data == "about":
        await query.edit_message_text(
            "ℹ️ مشروع شجرة العراق",
            reply_markup=main_keyboard()
        )


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lat = update.message.location.latitude
    lon = update.message.location.longitude

    await update.message.reply_text(
        f"""✅ تم استلام موقعك بنجاح.

📍 Latitude: {lat}
📍 Longitude: {lon}

الخطوة التالية:
📷 أرسل صورة الشجرة."""
    )


async def request_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if ":" not in text:
        return

    await update.message.reply_text(
        f"""✅ تم استلام طلب الشتلة بنجاح.

📋 البيانات المستلمة:

{text}

⏳ سيتم إرسال طلبك إلى المشرف للمراجعة.

بعد الموافقة سيصلك:

🌳 رقم الشتلة
📦 QR Code الخاص بالشتلة
📍 موقع الاستلام
📅 موعد الاستلام

شكراً لمساهمتك في مشروع شجرة العراق 🌳
"""
    )
    

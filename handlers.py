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
                        text="📍 إرسال موقعي",
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
        return

    messages = {
        "map": "🗺️ قريباً ستظهر الخريطة.",
        "profile": "👤 حسابك\n\n🌳 الأشجار: 0\n⭐ النقاط: 0",
        "leaders": "🏆 لوحة المتصدرين",
        "rewards": "🎁 المكافآت",
        "stats": "📊 الإحصائيات",
        "volunteer": "🤝 التطوع",
        "partners": "🏢 الشركاء",
        "news": "📢 الأخبار",
        "settings": "⚙️ الإعدادات",
        "about": "ℹ️ مشروع شجرة العراق",
    }

    await query.edit_message_text(
        messages.get(query.data, "اختر من القائمة"),
        reply_markup=main_keyboard()
    )


async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("LOCATION RECEIVED")

    await update.message.reply_text(
        "✅ وصل الموقع بنجاح."
    )


elif query.data == "request_tree":
    await query.edit_message_text(
        """🌱 طلب شتلة

لإرسال طلب شتلة اضغط الزر بالأسفل ثم اكتب معلوماتك بالترتيب:

• الاسم الكامل
• رقم الهاتف
• المحافظة
• القضاء
• المنطقة
• عدد الشتلات

مثال:

الاسم: أحمد علي
الهاتف: 07XXXXXXXXX
المحافظة: النجف القضاء: النالمنطقة:حي الامير
العدد: 3
""",
        reply_markup=main_keyboard()
    )

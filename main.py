from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = "8633332339:AAFaw4eQ09genK4d5luEoTgieGYzvmnoagk"

def main_keyboard():
    keyboard = [
        [InlineKeyboardButton("🌱 زرع شجرة", callback_data="plant"),
         InlineKeyboardButton("🗺️ الخريطة", callback_data="map")],

        [InlineKeyboardButton("👤 حسابي", callback_data="profile"),
         InlineKeyboardButton("🏆 المتصدرون", callback_data="leaders")],

        [InlineKeyboardButton("🎁 المكافآت", callback_data="rewards"),
         InlineKeyboardButton("📊 الإحصائيات", callback_data="stats")],

        [InlineKeyboardButton("🤝 التطوع", callback_data="volunteer"),
         InlineKeyboardButton("🏢 الشركاء", callback_data="partners")],

        [InlineKeyboardButton("📢 الأخبار", callback_data="news"),
         InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings")],

        [InlineKeyboardButton("ℹ️ عن المشروع", callback_data="about")]
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌳 أهلاً بك في مشروع شجرة العراق\n\nاختر الخدمة التي تريدها:",
        reply_markup=main_keyboard()
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "plant":
        text = """🌱 زرع شجرة

• تسجيل شجرة جديدة
• رفع صورة الشجرة
• تحديد الموقع
• متابعة حالة الطلب"""

    elif query.data == "map":
        text = """🗺️ الخريطة

هنا ستظهر جميع الأشجار المزروعة على الخريطة."""

    elif query.data == "profile":
        text = """👤 حسابي

الاسم: غير مسجل
النقاط: 0
عدد الأشجار: 0
الرتبة: مبتدئ"""

    elif query.data == "leaders":
        text = """🏆 المتصدرون

🥇 المركز الأول
🥈 المركز الثاني
🥉 المركز الثالث"""

    elif query.data == "rewards":
        text = """🎁 المكافآت

اجمع النقاط واستبدلها بجوائز."""

    elif query.data == "stats":
        text = """📊 الإحصائيات

🌳 الأشجار: 0
👥 المتطوعون: 0
🏢 الشركاء: 0"""

    elif query.data == "volunteer":
        text = """🤝 التطوع

سجل كمتطوع للمشاركة بزراعة الأشجار."""

    elif query.data == "partners":
        text = """🏢 الشركاء

لا يوجد شركاء حالياً."""

    elif query.data == "news":
        text = """📢 الأخبار

لا توجد أخبار جديدة."""

    elif query.data == "settings":
        text = """⚙️ الإعدادات

يمكنك تعديل إعدادات حسابك."""

    elif query.data == "about":
        text = """ℹ️ عن المشروع

مشروع شجرة العراق يهدف إلى زيادة المساحات الخضراء وتشجيع المواطنين على زراعة الأشجار."""

    else:
        text = "اختر من القائمة"

    await query.edit_message_text(
        text,
        reply_markup=main_keyboard()
    )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()

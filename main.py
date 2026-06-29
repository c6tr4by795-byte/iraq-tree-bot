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

    messages = {
        "plant": "🌱 قسم زرع شجرة",
        "map": "🗺️ قسم الخريطة",
        "profile": "👤 حسابي",
        "leaders": "🏆 لوحة المتصدرين",
        "rewards": "🎁 المكافآت",
        "stats": "📊 الإحصائيات",
        "volunteer": "🤝 التطوع",
        "partners": "🏢 الشركاء",
        "news": "📢 الأخبار",
        "settings": "⚙️ الإعدادات",
        "about": "ℹ️ مشروع شجرة العراق"
    }

    await query.edit_message_text(
        messages.get(query.data, "اختر من القائمة"),
        reply_markup=main_keyboard()
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()

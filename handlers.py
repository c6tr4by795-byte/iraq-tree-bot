from telegram import Update
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

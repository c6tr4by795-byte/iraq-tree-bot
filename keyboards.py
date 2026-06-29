from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("🌱 زرع شجرة", callback_data="plant"),
            InlineKeyboardButton("🗺️ الخريطة", callback_data="map"),
        ],
        [
            InlineKeyboardButton("🌿 طلب شتلة", callback_data="request_tree"),
        ],
        [
            InlineKeyboardButton("👤 حسابي", callback_data="profile"),
            InlineKeyboardButton("🏆 المتصدرون", callback_data="leaders"),
        ],
        [
            InlineKeyboardButton("🎁 المكافآت", callback_data="rewards"),
            InlineKeyboardButton("📊 الإحصائيات", callback_data="stats"),
        ],
        [
            InlineKeyboardButton("🤝 التطوع", callback_data="volunteer"),
            InlineKeyboardButton("🏢 الشركاء", callback_data="partners"),
        ],
        [
            InlineKeyboardButton("📢 الأخبار", callback_data="news"),
            InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
        ],
        [
            InlineKeyboardButton("ℹ️ عن المشروع", callback_data="about"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)

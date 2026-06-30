from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def admin_keyboard(user_id):
    keyboard = [
        [
            InlineKeyboardButton(
                "✅ موافقة",
                callback_data=f"approve_{user_id}"
            ),
            InlineKeyboardButton(
                "❌ رفض",
                callback_data=f"reject_{user_id}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

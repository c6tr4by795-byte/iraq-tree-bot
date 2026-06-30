from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def admin_keyboard(request_id):

    keyboard = [
        [
            InlineKeyboardButton(
                "✅ موافقة",
                callback_data=f"approve:{request_id}"
            ),
            InlineKeyboardButton(
                "❌ رفض",
                callback_data=f"reject:{request_id}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

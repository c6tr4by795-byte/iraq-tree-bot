from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from config import TOKEN
from handlers import start, buttons
from request_tree import request_data
from admin_handlers import admin_buttons

app = Application.builder().token(TOKEN).build()

# أمر البداية
app.add_handler(CommandHandler("start", start))

# أزرار المستخدم
app.add_handler(
    CallbackQueryHandler(
        buttons,
        pattern="^(request_tree|profile|map|leaders|rewards|stats|volunteer|partners|news|settings|about)$",
    )
)

# أزرار المشرف
app.add_handler(
    CallbackQueryHandler(
        admin_buttons,
        pattern="^(approve:|reject:).*",
    )
)

# استقبال رسائل المستخدم
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        request_data,
    )
)

app.run_polling()

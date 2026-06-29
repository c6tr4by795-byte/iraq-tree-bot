from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

from config import TOKEN
from handlers import start, buttons, location
from tree_requests import request_data

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.add_handler(MessageHandler(filters.LOCATION, location))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        request_data,
    )
)

app.run_polling()

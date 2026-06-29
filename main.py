from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import TOKEN
from handlers import start, buttons

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()

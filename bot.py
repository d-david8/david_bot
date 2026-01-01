from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.menu import menu
from handlers.start import start
from handlers.help import help
from handlers.profile import profile
from handlers.unregister import unregister
from services.broadcast import morning_greeting
from handlers.callbacks import button_handler
from handlers.weather import handle_city

import datetime
from telegram.ext import JobQueue
import logging

# Configure logging
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Register command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("profile", profile))
app.add_handler(CommandHandler("unregister", unregister))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_city))

logging.info("Bot started successfully.")

# Schedule daily morning greeting
# job_queue: JobQueue = app.job_queue
# job_queue.run_daily(
#     morning_greeting, time=datetime.time(hour=18, minute=40, second=0)
# )

# Start the bot
app.run_polling()

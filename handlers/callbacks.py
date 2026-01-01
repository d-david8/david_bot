from telegram import Update
from telegram.ext import ContextTypes
from handlers.profile import profile
from handlers.help import help
from handlers.unregister import unregister

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    chat = query.message

    if query.data == "weather":
        context.user_data["awaiting_city"] = True
        await chat.reply_text("🌍 Please enter a city name:")
    else:
        await chat.reply_text("Unknown option selected.")
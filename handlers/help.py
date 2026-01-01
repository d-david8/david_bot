# handlers/help.py
from telegram import Update
from telegram.ext import ContextTypes

# Help command handler
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    commands = (
        "🚀 /start - Start the bot and register yourself\n"
        "📋 /menu - Show the interactive menu\n"
        "ℹ️ /help - Show available commands\n"
        "👤 /profile - Show your saved data\n"
        "🗑️ /unregister - Remove your data from the bot"
    )
    await update.message.reply_text(f"📋 Available commands:\n{commands}")

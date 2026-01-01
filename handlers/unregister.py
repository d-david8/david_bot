# handlers/unregister.py
from telegram import Update
from telegram.ext import ContextTypes
from services.db import remove_user
import logging

async def unregister(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    unregister_status = remove_user(user.id)

    if unregister_status == "not_registered":
        await update.message.reply_text("You are not registered yet ⚠️.\nUse /start to register 🚀")
    elif unregister_status == "unregistered_successfully":
        await update.message.reply_text(f"👋Goodbye {user.first_name}!\nYour data has been removed 🗑️")
    else:
        await update.message.reply_text("An error occurred during unregistration ⚠️")

    logging.info(f"User {user.username} ({user.id}) used /unregister. Status: {unregister_status}")

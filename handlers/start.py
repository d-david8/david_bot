# handlers/start.py
import logging
from telegram import Update
from telegram.ext import ContextTypes
from services.db import add_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    registration_status = add_user(user.id, user.username, user.first_name, user.last_name, user.language_code)
    if registration_status == "already_registered":
        await update.message.reply_text("You are already registered 👋")
    elif registration_status == "registered_successfully":
        await update.message.reply_text(f"👋Hello {user.first_name}!\nDavid Bot is ready to assist you 🤖")
    else:
        await update.message.reply_text("An error occurred during registration ⚠️")

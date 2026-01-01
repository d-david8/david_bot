# handlers/profile.py
from telegram import Update
from telegram.ext import ContextTypes
from services.db import get_all_users, find_user

# Handler for the /profile command
async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_data = find_user(user_id)

    # Construct the response message
    if user_data:
        msg = (
            f"🆔 Telegram ID: {user_data['telegram_id']}\n"
            f"👤 Username: {user_data.get('username','-')}\n"
            f"📝 First Name: {user_data.get('first_name','-')}\n"
            f"📛 Last Name: {user_data.get('last_name','-')}\n"
            f"🌐 Language: {user_data.get('language_code','-')}"
        )
    else:
        msg = "You are not registered yet ⚠️.\nUse /start to register 🚀."
    await update.message.reply_text(msg)

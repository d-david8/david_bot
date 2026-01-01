from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from services.db import find_user

# Menu command handler
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Check if user is registered
    if not find_user(update.effective_user.id):
        await update.message.reply_text(
            "You are not registered yet ⚠️.\nUse /start to register 🚀."
        )
        return

    # Define the menu keyboard
    keyboard = [
        [InlineKeyboardButton("Weather 🌤️", callback_data="weather")]
    ]
    # Create the reply markup
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the menu message
    await update.message.reply_text(
        "Choose an option from the menu 👇",
        reply_markup=reply_markup
    )
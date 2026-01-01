import datetime
import logging
from services.db import get_all_users

async def morning_greeting(context):
    users = get_all_users()
    for user in users:
        try:
            await context.bot.send_message(
                chat_id=user["telegram_id"],
                text=f"☀️ Good morning! It's {datetime.datetime.now().strftime('%H:%M')}\nHave a great day! 🌟"
            )
        except Exception as e:
            logging.error(f"Error sending morning greeting to {user['telegram_id']}: {e}")  

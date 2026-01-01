from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TOKEN-ul Telegram nu este setat!")

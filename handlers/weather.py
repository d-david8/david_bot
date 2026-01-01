from telegram import Update
from telegram.ext import ContextTypes
from services.weather_api import get_weather

# Handler for processing city name input for weather information
async def handle_city(update: Update, context: ContextTypes.DEFAULT_TYPE):

    

    # Check if we are awaiting a city name
    if not context.user_data.get("awaiting_city"):
        return

    # Get the city name from the user's message
    city = update.message.text

    # Fetch weather data
    weather = get_weather(city)

    # If city not found, inform the user
    if not weather:
        await update.message.reply_text("❌ City not found. Try again.")
        return
    
    # Reset the awaiting city flag
    context.user_data["awaiting_city"] = False

    # Format and send the weather information
    msg = (
        f"🌦️ Weather in {city}\n\n"
        f"🌡️ Temperature: {weather['temp']}°C\n"
        f"🤔 Feels like: {weather['feels_like']}°C\n"
        f"💧 Humidity: {weather['humidity']}%\n"
        f"💨 Wind: {weather['wind']} km/h\n"
        f"☁️ {weather['description']}"
    )
    await update.message.reply_text(msg)

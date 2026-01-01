import requests

# Fetch weather data for a given city
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        # Make the API request
        r = requests.get(url, timeout=30)

        # Check for successful response
        if r.status_code != 200:
            return None

        # Parse the JSON response
        data = r.json()
        current = data["current_condition"][0]

        # Return relevant weather information
        return {
            "temp": current["temp_C"],
            "feels_like": current["FeelsLikeC"],
            "humidity": current["humidity"],
            "wind": current["windspeedKmph"],
            "description": current["weatherDesc"][0]["value"]
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

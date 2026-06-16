import requests
from langchain_core.tools import tool
from config import WEATHER_API_KEY


@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a city using Weatherstack.
    """

    url = "http://api.weatherstack.com/current"

    params = {
        "access_key": WEATHER_API_KEY,
        "query": city
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Handle API errors
        if "error" in data:
            return f"Weatherstack Error: {data['error']['info']}"

        current = data["current"]
        location = data["location"]

        return (
            f"📍 {location['name']}, {location['country']}\n"
            f"🌡 Temperature: {current['temperature']}°C\n"
            f"💧 Humidity: {current['humidity']}%\n"
            f"🌤 Weather: {', '.join(current['weather_descriptions'])}\n"
            f"💨 Wind Speed: {current['wind_speed']} km/h"
        )

    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"
    except Exception as e:
        return f"Unexpected Error: {e}"
    
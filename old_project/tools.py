
import requests
from langchain_core.tools import tool
from config import WEATHER_API_KEY

@tool
def get_weather(city:str)->str:
    '''Get current weather by city'''
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    try:
        r=requests.get(url,timeout=10)
        r.raise_for_status()
        d=r.json()
        return f"{d['name']}: {d['main']['temp']}°C, humidity {d['main']['humidity']}%, {d['weather'][0]['description']}"
    except Exception as e:
        return f"Error: {e}"

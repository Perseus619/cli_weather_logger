# import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime 
from zoneinfo import ZoneInfo
from weather.weather_fetcher import weather_fetcher

def date_convertor():
    weather_data, location = weather_fetcher()

    date = datetime.fromtimestamp(weather_data['dt'],ZoneInfo("Asia/Kolkata"))
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'],ZoneInfo("Asia/Kolkata"))
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'],ZoneInfo("Asia/Kolkata"))

    return date, sunrise, sunset, weather_data, location

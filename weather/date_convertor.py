from datetime import datetime 
from zoneinfo import ZoneInfo
from weather.weather_fetcher import weather_fetcher

def date_convertor():
    # Fetch the weather data and location using the weather_fetcher function
    weather_data, location = weather_fetcher()

    # Convert the main timestamp to a datetime object in Asia/Kolkata timezone
    date = datetime.fromtimestamp(weather_data['dt'], ZoneInfo("Asia/Kolkata"))
    # Convert the sunrise timestamp to a datetime object in Asia/Kolkata timezone
    sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'], ZoneInfo("Asia/Kolkata"))
    # Convert the sunset timestamp to a datetime object in Asia/Kolkata timezone
    sunset = datetime.fromtimestamp(weather_data['sys']['sunset'], ZoneInfo("Asia/Kolkata"))

    # Return the converted date, sunrise, sunset, along with weather data and location
    return date, sunrise, sunset, weather_data, location

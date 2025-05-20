weather_api = "https://api.openweathermap.org/data/2.5/weather"
geocoding_api = "http://api.openweathermap.org/geo/1.0/direct"
ip_geo_api = "http://ip-api.com/json"
api_key = "1cc39bd5a4e2e5a8d1bf2fd17048482e"

metrics_map = {
    "Temperature": ["main", "temp"],
    "Feels Like": ["main", "feels_like"],
    "Humidity": ["main", "humidity"],
    "Wind Speed": ["wind", "speed"],
    "Condition": ["weather", 0, "description"]
}

unit_map = {
    "Temperature":"\u00B0C",
    "Feels Like":"\u00B0C",
    "Humidity":"%",
    "Wind Speed":"m/s",
    "Condition":""
}
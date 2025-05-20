# import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from weather.weather_fetcher import weather_fetcher 
from config import metrics_map, unit_map
from weather.date_convertor import date_convertor

def extract_metrics():
    date, sunrise, sunset, weather_data, location = date_convertor()

    extracted = {}

    for key, path in metrics_map.items():
        try:   
            value = weather_data

            for p in path:
                value = value[p]
            extracted[key] = value
        
        except(KeyError,TypeError):
            extracted[key] = None

    
    unit = {}

    for key, value in extracted.items():
        units = unit_map.get(key,"")

        unit[key] = f" {value}{units}"
        
    
    final_metric = {
        "City":location,
        "Date":date,
        **unit,
        "Sunrise": sunrise,
        "Sunset": sunset
    }

    return final_metric








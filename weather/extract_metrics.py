from weather.weather_fetcher import weather_fetcher 
from config import metrics_map, unit_map
from weather.date_convertor import date_convertor

def extract_metrics():
    # Get the converted date, sunrise, sunset, weather data, and location
    date, sunrise, sunset, weather_data, location = date_convertor()

    extracted = {}  # Dictionary to store extracted metric values

    # Loop through each metric defined in metrics_map
    for key, path in metrics_map.items():
        try:   
            value = weather_data  # Start from the root of the weather data

            # Traverse the nested path to get the metric value
            for p in path:
                value = value[p]
            extracted[key] = value  # Store the extracted value
        
        except (KeyError, TypeError):
            # If the path is invalid or value is missing, set as None
            extracted[key] = None

    unit = {}  # Dictionary to store metric values with their units

    # Loop through each extracted metric to append units
    for key, value in extracted.items():
        units = unit_map.get(key, "")  # Get the unit for the metric (if any)
        unit[key] = f" {value}{units}"  # Format as " valueunit"
        
    # Prepare the final dictionary with all required weather metrics
    final_metric = {
        "City": location,
        "Date": date,
        **unit,           # Unpack all metrics with units
        "Sunrise": sunrise,
        "Sunset": sunset
    }

    return final_metric  # Return the final metrics dictionary








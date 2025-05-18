# import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import geocoding_api,api_key
import requests

def location_fetcher():
    location = input("Give Your Desired Location mate: ").strip().title()

    param = {
        "q": location,
        "limit":1,
        "appid": api_key
    }

    response = requests.get(geocoding_api,params=param)
    location_data = response.json()
    
    lat = location_data[0]['lat']
    lon = location_data[0]['lon']

    return lat, lon, location

# location_fetcher()



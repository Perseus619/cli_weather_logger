# import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import ip_geo_api
import requests

def ip_fetcher():
    response = requests.get(ip_geo_api)
    ip_data = response.json()

    lat = ip_data['lat']
    lon = ip_data['lon']
    location = ip_data['city']

    return lat, lon, location

# ip_fetcher()


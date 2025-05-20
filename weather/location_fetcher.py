import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import geocoding_api,api_key
import requests

def location_fetcher():
    
 while True:
   try:
    locate = input("Give Your Desired Location mate: ").strip().title()

    param = {
        "q": locate,
        "limit":1,
        "appid": api_key
    }

    response = requests.get(geocoding_api,params=param, timeout=5)
    response.raise_for_status()
    location_data = response.json()

    if not location_data:
     print("Location Error: No Location Found")
    else:
     lat = location_data[0]['lat']
     lon = location_data[0]['lon']
     location = location_data[0]['name']

     return lat, lon, location
   
   except requests.exceptions.ConnectionError:
    print("No Internet or DNS Failure")
   except requests.exceptions.Timeout:
    print("Request Timed Out")
   except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")
   except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}")
   except Exception as e: 
    print(f"Unexpected error: {type(e).__name__} - {e}")

   while True:
    retry1 = input("Do you want to retry (Y/N): ").title()

    if retry1 == 'Y':
     break
    elif retry1 == 'N':
     sys.exit()
    else:
     print("Invalid Input !!!")

# location_fetcher()






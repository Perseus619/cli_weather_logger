import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config import ip_geo_api
import requests

def ip_fetcher():
    
 while True:
   try: 
    response = requests.get(ip_geo_api, timeout=5)
    response.raise_for_status()
    ip_data = response.json()
    
    lat = ip_data['lat']
    lon = ip_data['lon']
    location = ip_data['city']

    return lat, lon, location
      
   except requests.exceptions.ConnectionError:
    print("No Internet or DNS Failure")
   except requests.exceptions.Timeout:
    print("The Request timed out")
   except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error: {http_err}")
   except requests.exceptions.RequestException as err:
    print(f"Request Error: {err}") 
   except Exception as e:
    print(f"Unexpected error: {type(e).__name__} - {e}")

   while True:
    try:
     retry = input("Do You Wanna Retrt(Y/N): ").title()
     if retry == "Y":
      break
     elif retry == "N":
      sys.exit()
    except ValueError:
     print("Invalid Input !!!")      




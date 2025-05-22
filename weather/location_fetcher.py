import sys
from config import geocoding_api, api_key
import requests

def location_fetcher():
    
 while True:
   try:
    # Prompt the user to enter their desired location
    locate = input("Give Your Desired Location mate: ").strip().title()

    # Prepare parameters for the geocoding API request
    param = {
        "q": locate,      # Location name entered by the user
        "limit": 1,       # Limit results to 1 location
        "appid": api_key  # API key for authentication
    }

    # Make a GET request to the geocoding API with a timeout of 5 seconds
    response = requests.get(geocoding_api, params=param, timeout=5)
    response.raise_for_status()  # Raise an error for bad HTTP status codes
    location_data = response.json()  # Parse the JSON response

    # Check if the API returned any location data
    if not location_data:
     print("Location Error: No Location Found")
    else:
     # Extract latitude, longitude, and location name from the response
     lat = location_data[0]['lat']
     lon = location_data[0]['lon']
     location = location_data[0]['name']

     # Return the latitude, longitude, and location name
     return lat, lon, location
   
   # Handle various exceptions that may occur during the API request
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

   # If an error occurred, prompt the user to retry or exit
   while True:
    retry1 = input("Do you want to retry (Y/N): ").title()

    if retry1 == 'Y':
     # Break inner loop to retry the API call
     break
    elif retry1 == 'N':
     # Exit the program if user chooses not to retry
     sys.exit()
    else:
     # Handle invalid input for retry prompt
     print("Invalid Input !!!")







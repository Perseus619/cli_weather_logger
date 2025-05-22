import sys
from config import ip_geo_api
import requests

def ip_fetcher():
    
 while True:
   try: 
    # Make a GET request to the IP geolocation API with a timeout of 5 seconds
    response = requests.get(ip_geo_api, timeout=5)
    response.raise_for_status()  # Raise an error for bad HTTP status codes
    ip_data = response.json()    # Parse the JSON response
    
    # Extract latitude, longitude, and city name from the response
    lat = ip_data['lat']
    lon = ip_data['lon']
    location = ip_data['city']

    # Return the latitude, longitude, and location name
    return lat, lon, location
      
   except requests.exceptions.ConnectionError:
    # Handle network connection errors
    print("No Internet or DNS Failure")
   except requests.exceptions.Timeout:
    # Handle request timeout errors
    print("The Request timed out")
   except requests.exceptions.HTTPError as http_err:
    # Handle HTTP errors (e.g., 404, 500)
    print(f"HTTP Error: {http_err}")
   except requests.exceptions.RequestException as err:
    # Handle other request-related errors
    print(f"Request Error: {err}") 
   except Exception as e:
    # Handle any other unexpected exceptions
    print(f"Unexpected error: {type(e).__name__} - {e}")

   # If an error occurred, prompt the user to retry or exit
   while True:
    try:
     retry = input("Do You Wanna Retrt(Y/N): ").title()
     if retry == "Y":
      # Break inner loop to retry the API call
      break
     elif retry == "N":
      # Exit the program if user chooses not to retry
      sys.exit()
    except ValueError:
     # Handle invalid input for retry prompt
     print("Invalid Input !!!")




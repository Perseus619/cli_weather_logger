import sys
import requests
from tabulate import tabulate
from config import weather_api, api_key
from weather.location_fetcher import location_fetcher
from weather.ip_fetcher import ip_fetcher

def weather_fetcher():
    
    # Display the menu for location selection
    print("Now,")
    menu = [
        ["Type 1 if you want to know the weather of your desired location "],
        ["Type 2 if you want to know weather of your current Location"] 
    ]

    print(tabulate(menu, headers="", tablefmt="grid"))

    while True:
        try:
            # Prompt the user to choose between manual location or current location
            user = input("\nMake Your Choice Mate: ")

            if user == '1':
                # User chooses to enter a desired location
                lat, lon, location = location_fetcher()

                # Prepare parameters for the weather API request
                param = {
                    "lat": lat,
                    "lon": lon,
                    "units": "metric",
                    "appid": api_key
                }

                # Attempt to fetch weather data for the chosen location
                while True:
                    try:
                        response = requests.get(weather_api, params=param)
                        weather_data = response.json()

                        # Return the weather data and location name
                        return weather_data, location
                     
                    except requests.exceptions.ConnectionError:
                        # Handle network connection errors
                        print("No Internet or DNS Failure")
                    except requests.exceptions.Timeout:
                        # Handle request timeout errors
                        print("Request Timed Out")
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
                        retry1 = input("Do you want to retry (Y/N): ").title()
                        if retry1 == 'Y':
                            break  # Break inner loop to retry API call
                        elif retry1 == 'N':
                            sys.exit()  # Exit the program
                        else:
                            print("Invalid Input !!!")     

            elif user == '2':
                # User chooses to use their current location (via IP)
                lat, lon, location = ip_fetcher()

                # Prepare parameters for the weather API request
                param = {
                    "lat": lat,
                    "lon": lon,
                    "units": "metric",
                    "appid": api_key
                }

                # Attempt to fetch weather data for the current location
                while True:
                    try:
                        response = requests.get(weather_api, params=param)
                        weather_data = response.json()

                        # Return the weather data and location name
                        return weather_data, location
                     
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
                            break
                        elif retry1 == 'N':
                            sys.exit()
                        else:
                            print("Invalid Input !!!")
           
            else:
                # Handle invalid menu input
                raise ValueError("Invalid Input Mate")

        except Exception as e:
            # Handle any error in the main menu selection
            print("Choose the appropiate option from the Menu")












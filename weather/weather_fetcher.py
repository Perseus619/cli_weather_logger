# import sys
# import os

# # Add the root project directory to sys.path dynamically
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from tabulate import tabulate
from config import weather_api, api_key
from weather.location_fetcher import location_fetcher
from weather.ip_fetcher import ip_fetcher

def weather_fetcher():
    
    print("Now,")
    menu = [
        ["Type 1 if you want to know the weather of your desired location "],
        ["Type 2 if you want to know weather of your current Location"] 
    ]

    print(tabulate(menu,headers="",tablefmt="grid"))

    while True:

        try:
           user = input("\nMake Your Choice Mate: ")

           if user == '1':
              lat, lon, location = location_fetcher()

              param = {
                  "lat":lat,
                  "lon":lon,
                  "units":"metric",
                  "appid":api_key
              }

              response = requests.get(weather_api,params=param)
              weather_data = response.json()

              return weather_data, location
           
           
           elif user == '2':
               lat, lon, location = ip_fetcher()

               param = {
                  "lat":lat,
                  "lon":lon,
                  "units":"metric",
                  "appid":api_key
              }

               response = requests.get(weather_api,params=param)
               weather_data = response.json()

               return weather_data, location
           
           else:
               raise ValueError("Invalid Input Mate")

        except Exception as e:
            print("Choose the appropiate option from the Menu")






    
    



    
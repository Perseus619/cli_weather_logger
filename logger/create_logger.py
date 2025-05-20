import csv
import os

def create_logg (weather_data):

    file_path = "Weather_log.csv"
    feild_names = ["City","Date","Temperature","Feels Like","Humidity","Wind Speed","Condition","Sunrise","Sunset"]

    if os.path.exists(file_path):

        with open(file_path, mode="a",  encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file,feild_names)
            writer.writerow(weather_data)

            print("Your Logger has been updated")

    else:

        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, feild_names)
            writer.writeheader()
            writer.writerow(weather_data)

            print("You Logger is created")





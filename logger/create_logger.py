import csv
import os

def create_logg(weather_data):
    # Define the path to the CSV file where weather logs will be stored
    file_path = "Weather_log.csv"
    # Define the field names (columns) for the CSV file
    feild_names = ["City", "Date", "Temperature", "Feels Like", "Humidity", "Wind Speed", "Condition", "Sunrise", "Sunset"]

    # Check if the log file already exists
    if os.path.exists(file_path):
        # If the file exists, open it in append mode to add new data
        with open(file_path, mode="a", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, feild_names)
            # Write the new weather data as a row in the CSV file
            writer.writerow(weather_data)
            print("Your Logger has been updated")
    else:
        # If the file does not exist, create it and write the header first
        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, feild_names)
            # Write the header row (column names)
            writer.writeheader()
            # Write the first weather data row
            writer.writerow(weather_data)
            print("You Logger is created")





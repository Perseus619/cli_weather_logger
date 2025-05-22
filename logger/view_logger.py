import os
import csv
import textwrap
from tabulate import tabulate
from filter.filter_weather import filter_weather



def view_logger():
    # Define the path to the weather log CSV file
    file_path = "Weather_log.csv"

    # Check if the log file exists
    if os.path.exists(file_path):
        # Open the CSV file in read mode
        with open(file_path, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            final_data = []
            
            # Iterate through each row in the CSV file
            for data in reader:
                # Wrap each value in the row for better table display
                wrapped_data = {
                    key: "\n".join(textwrap.wrap(value, width=14)) 
                    for key, value in data.items()
                }
                # Add the wrapped row to the final data list
                final_data.append(wrapped_data)

            # Display the weather log in a formatted table
            print(tabulate(final_data, headers="keys", tablefmt="fancy_grid"))

            # Offer filter options to the user for further data exploration
            filter_weather(final_data)
    else: 
        # If the log file does not exist, notify the user
        print("No Weather_log detected !!!\nFirst view the weather of any location to create a log")

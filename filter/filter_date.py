from tabulate import tabulate
from datetime import datetime

def filter_date(data):

    # Create a dictionary to store years as keys and sets of months as values
    date_show = dict()
    for items in data:
        # Clean and parse the date string from the data
        date_clean = items['Date'].split("\n")[0].strip()
        date_obj = datetime.strptime(date_clean, "%Y-%m-%d")
        month = date_obj.strftime("%B")
        year = date_obj.strftime("%Y")

        # Add the month to the set for the corresponding year
        if year not in date_show:
            date_show[year] = set()
        date_show[year].add(month)
    
    # Display the available years and their respective months
    print("List Of Months and Year")
    for year in date_show.keys():
        print(f"{year}")
        for month in date_show[year]:
            print(f"-{month}")

    # Start a loop to prompt the user for input until valid or exit
    while True:
        # Ask the user to input a month and year in the correct format
        user = input("Type the month and the respective year (eg: April 2025) - ").strip().replace(" ","")

        try:
            # Try to parse the user input into a datetime object
            date = datetime.strptime(user, "%B%Y")
        except ValueError:
            # If parsing fails, notify the user and offer to retry or quit
            print("Invalid Date Format !!!")
            user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
            if user1 == "Q":
                break
            else:
                continue

        # Filter the data for records matching the selected month and year
        filter_data = []
        for item in data:
            # Clean and parse the date for each record
            date_clean2 = item['Date'].split("\n")[0].strip()
            date_obj2 = datetime.strptime(date_clean2, "%Y-%m-%d")
    
            # Check if the year and month match the user's input
            if date_obj2.year == date.year and date_obj2.strftime("%B") == date.strftime("%B"):
                meta = {
                    "City": item["City"],
                    "Date": item["Date"],
                    "Temperature": item["Temperature"],
                    "Feels Like": item["Feels Like"],
                    "Humidity": item["Humidity"],
                    "Wind Speed": item["Wind Speed"],
                    "Condition": item["Condition"],
                    "Sunrise": item["Sunrise"],
                    "Sunset": item["Sunset"]
                }
                filter_data.append(meta)

        if filter_data:
            # If matching data is found, display it in a formatted table and exit
            print(f"Weather Record For: {date_obj2.strftime('%B')}, {date_obj2.year}".center(120, " "))
            print(tabulate(filter_data, headers="keys", tablefmt="fancy_grid"))
            break
        else:
            # If no data is found, notify the user and offer to retry or quit
            print("No Data Found for the input month and it's respective year")
            user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
            if user1 == "Q":
                break
            else:
                continue















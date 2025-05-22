from tabulate import tabulate
from datetime import datetime

def filter_date_city(data):

    # Collect all unique city names from the data
    city = set()
    for item in data:
        city.add(item["City"])
    
    # Prepare city names for display in a table
    city_print = [[x] for x in city]

    # Display the list of available cities
    print(tabulate(city_print, headers=["List Of Cities"], tablefmt="grid"))

    # Collect all unique years and months from the data
    date = dict()
    for item in data:
        # Extract the date part (in case there are newlines or extra info)
        date_clear = item["Date"].split("\n")[0]
        # Convert the string date to a datetime object
        date_obj = datetime.strptime(date_clear, "%Y-%m-%d")
        # Get the month name and year as strings
        month = date_obj.strftime("%B")
        year = date_obj.strftime("%Y")

        # Add the month to the set of months for the corresponding year
        if year not in date:
            date[year] = set()
        date[year].add(month)

    # Prepare the years and months for display
    for year, month in date.items():
        years = [year]
        months = month

    # Display the available years and months in a table
    print(tabulate([years, months], headers=["List Of Year & Month"], tablefmt="grid"))

    # Prompt the user to select a city from the list
    while True:
        user_location = input("Enter the name of the location from the list: ").strip().title()
        # Check if the entered city exists in the data
        if any(item["City"] == user_location for item in data):
            break
        else:
            print("Invalid Location !!!\nPlease choose from the list")
            user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
            if user1 == "Q":
                break
            else:
                continue

    # Prompt the user to select a month and year
    while True:
        while True:
            # Ask for month and year in the format "Month Year"
            user_date = input("Enter the month with respective year (eg- April 2025): ").strip().replace(" ", "")
            try:
                # Try to parse the input into a datetime object
                input_date = datetime.strptime(user_date, "%B%Y")
                break
            except ValueError:
                print("Invalid Date Format !!!")
                user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
                if user1 == "Q":
                    break
                else:
                    continue

        # Filter the data for the selected city and month/year
        filter_data = []
        for item in data:
            # Clean and parse the date
            date_clean2 = item['Date'].split("\n")[0].strip()
            date_obj2 = datetime.strptime(date_clean2, "%Y-%m-%d")

            # Check if both city and month/year match the user's input
            if (item["City"] == user_location and
                date_obj2.year == input_date.year and
                date_obj2.strftime("%B") == input_date.strftime("%B")):
                filter_data.append(
                    {
                        "Date": item["Date"],
                        "Temperature": item["Temperature"],
                        "Feels Like": item["Feels Like"],
                        "Humidity": item["Humidity"],
                        "Wind Speed": item["Wind Speed"],
                        "Condition": item["Condition"],
                        "Sunrise": item["Sunrise"],
                        "Sunset": item["Sunset"]  
                    }
                )

        # If matching data is found, display it in a table and exit
        if filter_data:
            print(tabulate(filter_data, headers="keys", tablefmt="fancy_grid"))
            break
        else:
            # If no data is found, inform the user and offer to retry or quit
            print("No Data Available !!! For the input month and year\nPlease Choose from the List")
            user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
            if user1 == "Q":
                break
            else:
                continue








from tabulate import tabulate

def filter_city(data):
    # Create a set to store unique city names from the data
    city = set()
    for items in data:
        city.add(items['City'])
    
    # Convert the set of cities into a list of lists for tabulate
    city_list = [[y] for y in city]

    # Display the list of available cities in a formatted table
    print(tabulate(city_list, headers=["List of Cities"], tablefmt="grid"))
    
    while True:
        # Prompt the user to enter the city name they want to view
        user = input("Type the name of the City you want to view : ").title().strip()

        city_data = []
        # Loop through the data to find records matching the user's city input
        for item in data:       
            if item["City"] == user:
                # Create a dictionary with relevant weather information
                meta = {
                    "Date": item["Date"],
                    "Temperature": item["Temperature"],
                    "Feels Like": item["Feels Like"],
                    "Humidity": item["Humidity"],
                    "Wind Speed": item["Wind Speed"],
                    "Condition": item["Condition"],
                    "Sunrise": item["Sunrise"],
                    "Sunset": item["Sunset"]
                }
                city_data.append(meta) 

        if city_data:
            # If data is found, display it in a formatted table and exit the loop
            print(f"Weather Data of: {user}".center(120, " "))
            print(tabulate(city_data, headers="keys", tablefmt="fancy_grid"))
            break
        else:
            # If no data is found, inform the user and offer to retry or quit
            print("Invalid Location Input\nChoose from the list")
            user1 = input("Type any key to continue or press (Q) to Exit: ").strip().upper()
            if user1 == "Q":
                break
            else:
                continue





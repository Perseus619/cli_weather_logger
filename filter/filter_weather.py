from tabulate import tabulate
from filter.filter_city import filter_city
from filter.filter_date import filter_date
from filter.filter_date_city import filter_date_city

def filter_weather(data):
    while True:
        # Ask the user if they want to use the filter functionality
        user = input("Do You want to use Filter mate (Y/N)?: ").upper()

        if user == "Y":
            # Show filter menu until a valid option is selected
            while True:
                menu = [
                    ["Type 1 to use Filter by City"],
                    ["Type 2 to use Filter by Month"],
                    ["Type 3 to use Filter for specific Location\nfor the specific month & year"]
                ]

                # Display the filter menu in a formatted table
                print(tabulate(menu, headers="", tablefmt="grid"))
                
                # Prompt the user to select a filter option
                user1 = input("Make You're choice mate: ")

                if user1 == "1":
                    # Call the function to filter by city
                    filter_city(data)
                    break
                elif user1 == "2":
                    # Call the function to filter by month/year
                    filter_date(data)
                    break
                elif user1 == "3":
                    # Call the function to filter by city and month/year
                    filter_date_city(data)
                    break
                else:
                    # Handle invalid menu input
                    print("Invalid Input !!!")
        elif user == "N":
            # Exit if the user does not want to use the filter
            break
        else:
            # Handle invalid input for the initial filter prompt
            print("Invalid Input !!!")





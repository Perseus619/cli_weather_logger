import time
import sys
from tabulate import tabulate

def nav():
    # Define the navigation menu options
    menu = [
        ["Type 1 to return to the Main Menu"],
        ["Type 2 to quit the Program"]
    ]

    # Display the menu in a formatted table
    print(tabulate(menu, headers="", tablefmt="grid"))
    
    while True:
        try:
            # Prompt the user for their choice
            user = input("Make your choice mate - ")

            if user == "1":
                # If user selects 1, return to the main menu
                print("Returning to the Main Menu")
                time.sleep(1)  # Pause for user experience
                break
            elif user == "2":
                # If user selects 2, exit the program
                print("Thank You For Using The Weather Logger")
                time.sleep(1)  # Pause before exiting
                sys.exit()
            else:
                # Raise an error for any invalid input
                raise ValueError("Invalid Input!!")
        except ValueError as e:
            # Display the error message and prompt again
            print(e)
            time.sleep(1)  # Pause before re-prompting


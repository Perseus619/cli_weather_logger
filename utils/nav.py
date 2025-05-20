import time
import sys
from tabulate import tabulate

def nav():

    menu = [
        ["Type 1 to return to the Main Menu"],
        ["Type 2 to quit the Program"]
    ]

    print(tabulate(menu, headers="", tablefmt="grid"))
    
    while True:
      try:
        user = input("Make your choice mate - ")

        if user == "1":
            print("Returning to the Main Menu")
            time.sleep(1)
            break
        elif user == "2":
            print("Thank You For Using The Weather Logger")
            time.sleep(1)
            sys.exit()
        else:
            raise ValueError("Invalid Input!!")
      except ValueError as e:
         print(e)
         time.sleep(1)
        
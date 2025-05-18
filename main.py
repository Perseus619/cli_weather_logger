import time
from tabulate import tabulate
from weather.print_weather import print_weather

def main():

    
    print("Weather Logger".center(50,(".")))
    print("[Log weather of anywhere in the world]".center(50,(" ")))
    print("\n")
    
    menu = [
     ["1. Type 1 to View Weather"],
     ["2. Type 2 to View the Logger"],
     ["3. Type 3 to Quit the Program"],
    ]

    print(tabulate(menu,headers="",tablefmt='grid'))
    print("\n")

    while True:
     try:
        user = input("Make your choice mate - ").strip()
        if user == "1":
          print_weather()
          break
        elif user == "2":
          #  view_logger() 
          print(1)
        elif user == "3":
           print("Thank You For Using Weather Logger")
           time.sleep(1)
           break
        else:
          raise ValueError("Mate please give an appropiate input")     
     except ValueError as e :
         print(e)
         time.sleep(1)

main()

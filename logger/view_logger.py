import os
import csv
import textwrap
from tabulate import tabulate


def view_logger():

  file_path = "Weather_log.csv"

  if os.path.exists(file_path):
      with open(file_path, mode="r", encoding="utf-8", newline="") as file:
         reader = csv.DictReader(file)
         final_data = []
         
         for data in reader:
            wrapped_data = {
               key: "\n".join(textwrap.wrap(value,width=14)) 
               for key, value in data.items()
            }
              
            final_data.append(wrapped_data)

         print(tabulate(final_data,headers="keys",tablefmt="fancy_grid"))

  else: 
     print("No Weather_log detected !!!\nFirst view the weather of any location to create a log")


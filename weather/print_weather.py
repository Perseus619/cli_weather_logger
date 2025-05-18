import sys
import os

# Add the root project directory to sys.path dynamically
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tabulate import tabulate
from weather.extract_metrics import extract_metrics

def print_weather():
    weather_data = extract_metrics()

    print_data = [[x,y] for x,y in weather_data.items()]

    return print(tabulate(print_data,headers=['Metrics','Value'],tablefmt="fancy_grid"))


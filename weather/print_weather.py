from tabulate import tabulate
from weather.extract_metrics import extract_metrics
from logger.create_logger import create_logg

def print_weather():
    weather_data = extract_metrics()

    print_data = [[x,y] for x,y in weather_data.items()]

    print(tabulate(print_data,headers=['Metrics','Value'],tablefmt="fancy_grid"))
    
    create_logg(weather_data)

    



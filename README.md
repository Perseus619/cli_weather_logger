# CLI Weather Logger

A simple and interactive command-line application to fetch, display, and log weather data for any city in the world. View current weather, maintain a log, and filter historical weather records with ease.

## Features

- **Fetch Weather:** Get real-time weather for any city or your current location.
- **Log Weather:** Automatically logs weather data to `Weather_log.csv`.
- **View Logs:** Display all logged weather data in a neat table format.
- **Filter Logs:** Filter weather logs by city, month/year, or both.
- **User-Friendly Navigation:** Simple menu-driven interface with clear prompts and error handling.

## How It Works

1. **Menu Navigation:**  
   On running the script, you'll see a menu with options to view weather, view the logger, or quit the program.

2. **Fetching Weather:**  
   Choose to fetch weather for your current location or any city. Data is fetched from OpenWeatherMap and logged in `Weather_log.csv`.

3. **Viewing & Filtering Logs:**  
   View all logged weather data in a table. Use filters to see logs by city, month, year, or both.

## Requirements

- Python 3.10+
- [tabulate](https://pypi.org/project/tabulate/)
- [requests](https://pypi.org/project/requests/)

Install dependencies with:
```bash
pip install tabulate requests
```

## Usage

Run the script from your terminal:
```bash
python main.py
```

Follow the on-screen prompts to fetch weather, view logs, or filter records.

## Data Storage

All weather data is stored in a local `Weather_log.csv` file in the project directory.

## Example

```
.....................Weather Logger.....................
      [Log weather of anywhere in the world]


+-------------------------------+
| 1. Type 1 to View Weather     |
| 2. Type 2 to View the Logger  |
| 3. Type 3 to Quit the Program |
+-------------------------------+
```

## License

This project is for personal use and learning purposes.

---

**Happy Logging!**
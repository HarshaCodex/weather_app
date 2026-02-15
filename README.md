# Weather App

A simple Python-based weather application that fetches and displays weather data for a given location using the Open-Meteo API.

## Features

- **GUI Interface (PyQt5)**: User-friendly interface to search for improved weather details.
- **Dynamic Weather Display**: Shows current temperature, temperature range, elevation, and timezone.
- **Interactive CLI**: Command-line interface for quick weather checks.
- **Data Models**: Structured Pydantic models for API responses.

## Project Structure

```
weather_app/
├── client/
│   └── weather_client.py       # API client for fetching weather data
├── models/
│   ├── coordinates.py          # Coordinates data model
│   ├── geocoding_response.py   # Geocoding API response model
│   └── weather_response.py     # Weather API response model
├── service/
│   └── interactive_cli.py      # CLI service logic
├── ui/
│   └── main.py                 # PyQt5 Main Window implementation
├── util/
│   ├── constants.py            # Application constants
│   └── weather_util.py         # Utility functions
├── app.py                      # Main entry point for the GUI app
└── cli_tool.py                 # Entry point for the CLI tool
```

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/HarshaCodex/weather_app.git
   cd weather_app
   ```

2. **Install Dependencies:**
   Ensure you have Python 3.x installed. Install the required packages:
   ```bash
   pip3 install requests pydantic PyQt5
   ```

## Usage

### Running the GUI Application
To launch the graphical user interface:
```bash
python3 app.py
```
Enter a city name in the search bar and click "Search" to view the weather details.

### Running the CLI Tool
To use the command-line interface:
```bash
python3 cli_tool.py
```
Follow the prompts to enter a city name.

## API Reference

This application uses the [Open-Meteo API](https://open-meteo.com/):
- **Geocoding API**: To convert city names to coordinates.
- **Forecast API**: To fetch weather data based on coordinates.

## License

This project is open-source and available for personal and educational use.

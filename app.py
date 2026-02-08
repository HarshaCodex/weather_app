from util.constants import TEMPERATURE_2M
from exception.WeatherException import WeatherException
from models.coordinates import Coordinates
from models.weather_response import WeatherResponse
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

url = os.getenv('OPEN_WEATHER_URL')

def get_weather_by_coordinates(coordinates: Coordinates):
    try:
        params = {
            'latitude': coordinates.latitude,
            'longitude': coordinates.longitude,
            'hourly': TEMPERATURE_2M
        }
        
        r = requests.get(url, params=params)
        
        if r.status_code != 200:
            raise WeatherException(r.status_code, f"API request failed: {r.text}")
        
        return WeatherResponse.model_validate_json(r.text)
    except requests.RequestException as e:
        raise WeatherException(500, f"Network error: {str(e)}")
    except WeatherException:
        raise

if __name__ == "__main__":
    try:
        coordinates = Coordinates()
        coordinates.latitude = 52.52
        coordinates.longitude = 13.41

        weather = get_weather_by_coordinates(coordinates)
        
        print(f"Location: {weather.latitude}, {weather.longitude}")
        print(f"Elevation: {weather.elevation}m")
        print(f"Timezone: {weather.timezone}")
        print(f"\nCurrent Temperature: {weather.get_current_temperature()}°C")
        
        min_temp, max_temp = weather.get_temperature_range()
        print(f"Temperature Range: {min_temp}°C to {max_temp}°C")
        print(f"Temperature Range (F): {weather.celsius_to_fahrenheit(min_temp):.1f}°F to {weather.celsius_to_fahrenheit(max_temp):.1f}°F")
        
    except WeatherException as e:
        print(f"Error: {e}")

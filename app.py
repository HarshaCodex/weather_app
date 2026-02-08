from client.weather_client import WeatherClient
from util.constants import TEMPERATURE_2M
from exception.WeatherException import WeatherException
from models.coordinates import Coordinates

if __name__ == "__main__":
    try:
        weather_client = WeatherClient()

        coordinates = Coordinates()
        coordinates.latitude = 52.52
        coordinates.longitude = 13.41

        weather = weather_client.get_weather_by_coordinates(coordinates=coordinates)
        
        print(f"Location: {weather.latitude}, {weather.longitude}")
        print(f"Elevation: {weather.elevation}m")
        print(f"Timezone: {weather.timezone}")
        print(f"\nCurrent Temperature: {weather.get_current_temperature()}°C")
        
        min_temp, max_temp = weather.get_temperature_range()
        print(f"Temperature Range: {min_temp}°C to {max_temp}°C")
        print(f"Temperature Range (F): {weather.celsius_to_fahrenheit(min_temp):.1f}°F to {weather.celsius_to_fahrenheit(max_temp):.1f}°F")

        weather_by_city = weather_client.get_weather_by_city(city='New York')

        print(f"\nWeather by city:{weather_by_city.get_current_temperature()}°C")
        
    except WeatherException as e:
        print(f"Error: {e}")

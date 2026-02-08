from client.weather_client import WeatherClient
from models.coordinates import Coordinates
from exception.WeatherException import WeatherException

def interactive_cli():
    weather_client = WeatherClient()
    
    while True:
        print("\n--- Weather CLI Menu ---")
        print("1. Get weather by city name")
        print("2. Get weather by coordinates (lat, long)")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == '1':
            city = input("Enter city name: ").strip()
            if not city:
                print("City name cannot be empty.")
                continue
            try:
                weather = weather_client.get_weather_by_city(city)
                display_weather(weather)
            except WeatherException as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            try:
                lat_str = input("Enter latitude: ").strip()
                lon_str = input("Enter longitude: ").strip()
                lat = float(lat_str)
                lon = float(lon_str)
                coords = Coordinates()
                coords.latitude = lat
                coords.longitude = lon
                weather = weather_client.get_weather_by_coordinates(coords)
                display_weather(weather)
            except ValueError:
                print("Invalid input. Please enter numeric values for coordinates.")
            except WeatherException as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def display_weather(weather):
    print(f"\nLocation: {weather.latitude}, {weather.longitude}")
    print(f"Elevation: {weather.elevation}m")
    print(f"Timezone: {weather.timezone}")
    print(f"Current Temperature: {weather.get_current_temperature()}°C")
    
    min_temp, max_temp = weather.get_temperature_range()
    print(f"Temperature Range: {min_temp}°C to {max_temp}°C")
    print(f"Temperature Range (F): {weather.celsius_to_fahrenheit(min_temp):.1f}°F to {weather.celsius_to_fahrenheit(max_temp):.1f}°F")

if __name__ == "__main__":
    interactive_cli()
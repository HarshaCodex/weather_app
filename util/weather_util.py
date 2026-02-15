def display_weather(weather):
    print(f"\nLocation: {weather.latitude}, {weather.longitude}")
    print(f"Elevation: {weather.elevation}m")
    print(f"Timezone: {weather.timezone}")
    print(f"Current Temperature: {weather.get_current_temperature()}°C")
    
    min_temp, max_temp = weather.get_temperature_range()
    print(f"Temperature Range: {min_temp}°C to {max_temp}°C")
    print(f"Temperature Range (F): {weather.celsius_to_fahrenheit(min_temp):.1f}°F to {weather.celsius_to_fahrenheit(max_temp):.1f}°F")

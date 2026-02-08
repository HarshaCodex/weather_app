from service.interactive_cli import interactive_cli
from exception.WeatherException import WeatherException

if __name__ == "__main__":
    try:
        interactive_cli()
    except WeatherException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")

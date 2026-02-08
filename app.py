from ui.main import window
from service.interactive_cli import interactive_cli
from exception.WeatherException import WeatherException

if __name__ == "__main__":
    try:
        window()
    except WeatherException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGoodbye!")

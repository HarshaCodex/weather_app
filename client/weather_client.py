from models.geocoding_response import GeocodingResponse
from util.constants import TEMPERATURE_2M
from models.coordinates import Coordinates
from models.weather_response import WeatherResponse
from exception.WeatherException import WeatherException
import requests

class WeatherClient():
    def get_weather_by_city(self, city: str, count: int = 1):
        try:
            url = "https://geocoding-api.open-meteo.com/v1/search"
            params = {
                'name': city.lower(),
                'count': count
            }
            response = requests.get(url, params=params)
            
            if response.status_code != 200:
                raise WeatherException(response.status_code, response.text)
            
            city_location_results = GeocodingResponse.model_validate_json(response.text)
            
            if city_location_results.results != 0:
                coordinates = Coordinates()
                coordinates.latitude = city_location_results.results[0].latitude
                coordinates.longitude = city_location_results.results[0].longitude
                return self.get_weather_by_coordinates(coordinates=coordinates)
            else:
                raise WeatherException(404, f"No results found for city:{city}")
        except requests.RequestException as e:
            raise WeatherException(500, f"Network error: {str(e)}")
        except WeatherException:
            raise

    def get_weather_by_coordinates(self, coordinates: Coordinates):
        try:
            url = "https://api.open-meteo.com/v1/forecast"
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



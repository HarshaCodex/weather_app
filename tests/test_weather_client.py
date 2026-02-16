from unittest.mock import patch, Mock
import pytest
from client.weather_client import WeatherClient
from exception.WeatherException import WeatherException
from models.coordinates import Coordinates
from models.weather_response import WeatherResponse

@pytest.fixture
def weather_client():
    return WeatherClient()

@patch('client.weather_client.requests.get')
def test_get_weather_by_city_success(mock_get, weather_client):
    # Mock geocoding response
    mock_geo_response = Mock()
    mock_geo_response.status_code = 200
    mock_geo_response.text = '{"results": [{"id": 1, "name": "New York", "latitude": 40.7128, "longitude": -74.0060, "generationtime_ms": 0.5}], "generationtime_ms": 0.5}'
    
    # Mock weather response
    mock_weather_response = Mock()
    mock_weather_response.status_code = 200
    mock_weather_response.text = '{"latitude": 40.7128, "longitude": -74.0060, "generationtime_ms": 0.5, "utc_offset_seconds": 0, "timezone": "America/New_York", "timezone_abbreviation": "EST", "elevation": 10.0, "hourly_units": {"time": "iso8601", "temperature_2m": "°C"}, "hourly": {"time": ["2023-10-27T00:00"], "temperature_2m": [15.0]}}'

    # Configure side_effect to return different responses for sequential calls
    mock_get.side_effect = [mock_geo_response, mock_weather_response]

    result = weather_client.get_weather_by_city('New York')
    
    assert isinstance(result, WeatherResponse)
    assert result.latitude == 40.7128
    assert result.longitude == -74.0060
    assert mock_get.call_count == 2

@patch('client.weather_client.requests.get')
def test_get_weather_by_city_not_found(mock_get, weather_client):
    mock_response = Mock()
    mock_response.status_code = 200
    # Simulate API returning no results
    mock_response.text = '{"results": [], "generationtime_ms": 0.5}' 
    
    mock_get.return_value = mock_response
    
    with pytest.raises(WeatherException) as excinfo:
        weather_client.get_weather_by_city('Unknown City')
    
    assert "No results found for city" in str(excinfo.value)

@patch('client.weather_client.requests.get')
def test_get_weather_by_city_api_failure(mock_get, weather_client):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_get.return_value = mock_response

    with pytest.raises(WeatherException) as excinfo:
        weather_client.get_weather_by_city('City')
    
    assert str(500) in str(excinfo.value)

@patch('client.weather_client.requests.get')
def test_get_weather_by_coordinates_success(mock_get, weather_client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = '{"latitude": 40.7128, "longitude": -74.0060, "generationtime_ms": 0.5, "utc_offset_seconds": 0, "timezone": "America/New_York", "timezone_abbreviation": "EST", "elevation": 10.0, "hourly_units": {"time": "iso8601", "temperature_2m": "°C"}, "hourly": {"time": ["2023-10-27T00:00"], "temperature_2m": [15.0]}}'
    mock_get.return_value = mock_response

    coords = Coordinates(latitude=40.7128, longitude=-74.0060)
    result = weather_client.get_weather_by_coordinates(coords)

    assert isinstance(result, WeatherResponse)
    assert result.latitude == 40.7128

@patch('client.weather_client.requests.get')
def test_get_weather_by_coordinates_api_failure(mock_get, weather_client):
    mock_response = Mock()
    mock_response.status_code = 400
    mock_response.text = "Bad Request"
    mock_get.return_value = mock_response

    coords = Coordinates(latitude=40.7128, longitude=-74.0060)
    with pytest.raises(WeatherException) as excinfo:
        weather_client.get_weather_by_coordinates(coords)
    
    assert str(400) in str(excinfo.value)
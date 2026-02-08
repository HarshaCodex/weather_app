from pydantic import BaseModel
from typing import List


class HourlyUnits(BaseModel):
    time: str
    temperature_2m: str


class HourlyData(BaseModel):
    time: List[str]
    temperature_2m: List[float]


class WeatherResponse(BaseModel):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: float
    hourly_units: HourlyUnits
    hourly: HourlyData
    
    def get_current_temperature(self) -> float:
        if self.hourly.temperature_2m:
            return self.hourly.temperature_2m[0]
        return 0.0
    
    def get_temperature_range(self) -> tuple[float, float]:
        temps = self.hourly.temperature_2m
        return (min(temps), max(temps)) if temps else (0.0, 0.0)
    
    def celsius_to_fahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32

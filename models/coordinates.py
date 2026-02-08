from pydantic import Field
from pydantic import BaseModel

class Coordinates(BaseModel):
    latitude: float = Field(default=0.0)
    longitude: float = Field(default=0.0)
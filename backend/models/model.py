from pydantic import BaseModel, Field
import uuid

from bson import ObjectId

class Datos_sensor(BaseModel):
    _id: ObjectId  # Use ObjectId type
    temperatura: float
    rh: float
    dew_point: float
    rain: float
    wind_speed: float
    gust_speed: float
    wind_direction: float

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {"_id":  "6591ef5527d8fe5017392a4c",
                        "temperatura": 23.41535119,
                        "rh":  84.20419048,
                        "dew_point": 20.1311627,
                        "rain":  0.001984127,
                        "wind_speed":  0.196924603,
                        "gust_speed":  0.94796627,
                        "wind_direction":  173.0823413}
        }


class Datos_manuales(BaseModel):
    fruto: int
    severidad: int

class Prediccion(BaseModel):
    incidencia:int

class Datos_manuales(BaseModel):
    fruto:int
    severidad:int

class Estaciones(BaseModel):
    estacion:str
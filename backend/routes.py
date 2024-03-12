from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from models.model import Datos_sensor, Prediccion, Datos_manuales, Estaciones
from typing import List
import numpy as np

router = APIRouter()


@router.post("/predict", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Prediccion)
def obtener_prediccion_actual(request: Request, datos_manules: Datos_manuales = Body(...)):
    datos_manules = jsonable_encoder(datos_manules)
    datos_sensores: List[Datos_sensor] = list(
        request.app.database["sacha"].find().sort([('_id', -1)]).limit(1))

    X_test = np.array([
        datos_manules["fruto"], datos_manules["severidad"], datos_sensores[0][
            "rain"], datos_sensores[0]["temperatura"], datos_sensores[0]["rh"],
        datos_sensores[0]["dew_point"], datos_sensores[0]["wind_speed"],
        datos_sensores[0]["gust_speed"],
        datos_sensores[0]["wind_direction"]
    ])
    prediction = request.app.model.predict(X_test.reshape(1, -1))
    return {"incidencia": prediction[0]}


@router.post("/data", response_description="Create a new book", status_code=status.HTTP_201_CREATED, response_model=Prediccion)
def obtener_prediccion_sonar(request: Request, data=Body()):
    try:
        data_ = jsonable_encoder(data)

        # Convierte explícitamente a tipo numérico
        X_test = np.array([
            float(data_["Total commits"]),
            float(data_["Total commits per day"]),
            float(data_["Accumulated commits"]),
            float(data_["Committers"]),
            float(data_["Committers Weight"])
        ])

        # Asegúrate de que tenga la forma correcta (1, 5)
        X_test = X_test.reshape(1, -1)

        prediction = request.app.model.predict(X_test)

        return {"incidencia": prediction[0]}
    except Exception as e:
        print(f"Error during prediction: {e}")
        raise

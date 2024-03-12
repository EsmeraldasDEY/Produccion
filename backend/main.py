from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router
import joblib  # importa las bibliotecas joblib para cargar el
from fastapi.middleware.cors import CORSMiddleware

config = dotenv_values(".env")

origins = [
    "*"
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    model = joblib.load('./in/best_model_0.998.pkl')
    app.model = model
    yield
    app.mongodb_client.close()

# @app.on_event("startup")
# def startup_db_client():
#     app.mongodb_client = MongoClient(config["ATLAS_URI"])
#     app.database = app.mongodb_client[config["DB_NAME"]]

#     print("hola")


# @app.get("/")
# async def read_root():
#     print(app.database['login'].find_one())
#     return {"Hello": "World"}

app = FastAPI(lifespan=lifespan)
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
     
    )

app.include_router(router)

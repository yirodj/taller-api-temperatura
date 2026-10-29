"""API REST de demostración para Google Colab -> GitHub -> Render -> Flutter."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from conversor import celsius_a_fahrenheit

app = FastAPI(
    title="API de Temperaturas - Taller Python a Flutter",
    description="Convierte grados Celsius a Fahrenheit para la práctica del taller.",
    version="1.0.0",
)

# Para la demostración en Flutter Web. En una API real, limitar orígenes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class TemperaturaEntrada(BaseModel):
    celsius: float = Field(..., description="Temperatura expresada en grados Celsius")


@app.get("/", tags=["Estado"])
def inicio():
    return {"mensaje": "API activa", "documentacion": "/docs"}


@app.post("/convertir", tags=["Conversión"])
def convertir(datos: TemperaturaEntrada):
    return {
        "celsius": datos.celsius,
        "fahrenheit": celsius_a_fahrenheit(datos.celsius),
    }

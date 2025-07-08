# backend/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "¡Marca Chancho API funcionando correctamente!"}

@app.get("/buscar")
def buscar_producto(q: str):
    return {"producto_buscado": q}
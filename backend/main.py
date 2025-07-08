import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/buscar")
def buscar_producto(q: str):
    app_id = os.getenv("ALIEXPRESS_APP_ID")
    url = "https://marca-chancho.onrender.com/buscar"  # Reemplazá con el endpoint real

    params = {
        "app_id": app_id,
        "keywords": q,
        "page": 1,
        "page_size": 5
    }

    try:
        response = httpx.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Adaptar según la estructura real de la API
        resultados = [
            {
                "nombre": item["title"],
                "precio": item["price"],
                "imagen": item["image_url"],
                "link": item["product_url"]
            }
            for item in data["products"]
        ]

        return {"resultados": resultados}

    except Exception as e:
        return {"error": str(e)}

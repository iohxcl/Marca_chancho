# backend/main.py

import os
import time
import httpx
import hmac
import hashlib
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

# 🔐 Cargar variables de entorno
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# 🚀 Inicializar FastAPI
app = FastAPI()

# 🌐 Configurar CORS para permitir llamadas desde frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Podés restringir a tu dominio luego
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Función para generar firma AliExpress
def generar_firma(app_secret: str, params: Dict[str, str]) -> str:
    sorted_params = sorted(params.items())
    concatenated = ''.join(f"{k}{v}" for k, v in sorted_params)
    base_string = f"{app_secret}{concatenated}{app_secret}"
    signature = hmac.new(
        app_secret.encode("utf-8"),
        base_string.encode("utf-8"),
        hashlib.sha1
    ).hexdigest().upper()
    return signature

# 🔎 Ruta principal de búsqueda
@app.get("/buscar")
def buscar_producto(q: str = Query(..., description="Palabra clave para buscar productos")):
    app_id = os.getenv("ALIEXPRESS_APP_ID")
    app_secret = os.getenv("ALIEXPRESS_APP_SECRET")

    if not app_id or not app_secret:
        raise RuntimeError("⚠️ Faltan credenciales. Revisá tu archivo .env")

    timestamp = int(time.time() * 1000)

    params = {
        "app_key": app_id,
        "timestamp": str(timestamp),
        "keywords": q,
        "fields": "productId,productTitle,productUrl,imageUrl,salePrice",
        "sort": "commissionRateDown",
        "page_size": "10"
    }

    # Generar firma
    sign = generar_firma(app_secret, params)
    params["sign"] = sign

    url = f"https://api.aliexpress.com/openapi/param2/2/portals.open/api.listPromotionProduct/{app_id}"

    try:
        response = httpx.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        productos = [
            {
                "nombre": item["productTitle"],
                "precio": item["salePrice"],
                "imagen": item["imageUrl"],
                "link": item["productUrl"]
            }
            for item in data.get("result", {}).get("products", [])
        ]

        return {"resultados": productos}

    except Exception as e:
        return {"error": str(e)}
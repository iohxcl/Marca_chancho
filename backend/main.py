import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path
import os

# 🔐 Cargar .env desde la carpeta actual (backend/)
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# ✅ Obtener el App ID de forma segura
app_id = os.getenv("ALIEXPRESS_APP_ID")
if not app_id:
    raise RuntimeError("⚠️ ALIEXPRESS_APP_ID no está definido. Verificá tu archivo .env.")

# 🚀 Inicializar FastAPI
app = FastAPI()

# 🌐 Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔎 Endpoint de búsqueda
@app.get("/buscar")
def buscar_producto(q: str):
    url = "https://marca-chancho.onrender.com/buscar"  # Reemplazá con el endpoint real de AliExpress

    params = params = {
    "q": q
}
    print("✅ Params cargados:", params)

    try:
        response = httpx.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # 🧠 Adaptar según la estructura real de la respuesta
        resultados = [
            {
                "nombre": item["title"],
                "precio": item["price"],
                "imagen": item["image_url"],
                "link": item["product_url"]
            }
            for item in data.get("products", [])
        ]

        return {"resultados": resultados}

    except Exception as e:
        return {"error": str(e)}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "¡Marca Chancho API está viva!"}

@app.get("/buscar")
def buscar_producto(q: str):
    return {
        "resultados": [
            {
                "nombre": f"{q} Pro Max",
                "precio": "$19.99",
                "imagen": "https://via.placeholder.com/150",
                "link": "https://aliexpress.com/item/123"
            },
            {
                "nombre": f"{q} Lite",
                "precio": "$9.99",
                "imagen": "https://via.placeholder.com/150",
                "link": "https://aliexpress.com/item/456"
            }
        ]
    }
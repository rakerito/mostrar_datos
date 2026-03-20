from fastapi import FastAPI

app = FastAPI()

# Datos de prueba (Simulando una base de datos)
products = [
    {"id": "1", "name": "Laptop", "price": 1200.0},
    {"id": "2", "name": "Mouse", "price": 25.0},
    
]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: str):
    return next((p for p in products if p["id"] == product_id), {"error": "No encontrado"})
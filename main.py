from fastapi import FastAPI
import json

app = FastAPI(
    title="Public Products API",
    description="A simple public API that returns e-commerce product data.",
    version="1.0.0"
)
@app.get("/products")
def get_all_products():
    return products


# Load JSON file
with open("products.json", "r") as file:
    products = json.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to the Public Products API!"}

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: str):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

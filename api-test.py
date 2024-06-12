from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import requests

app = FastAPI()

# Dados estáticos de exemplo para caldos e proteínas
broths = ["Shoyu", "Miso", "Tonkotsu", "Shio"]
proteins = ["Chicken", "Pork", "Beef", "Tofu"]

# Modelo para o pedido
class OrderRequest(BaseModel):
    broth: str
    protein: str
    
# Modelo para a resposta do pedido
class OrderResponse(BaseModel):
    order_id: str
    message: str
    
# Endpoint para listar caldos
@app.get("/broths", response_model=list)
async def get_broths():
    return broths

# Endpoint para listar proteínas
@app.get("/proteins", response_model=list)
async def get_proteins():
    return proteins
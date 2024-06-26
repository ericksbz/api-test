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

# Função para gerar o ID do pedido
def generate_order_id(api_key: str) -> str:
    url = "https://api.tech.redventures.com.br/orders/generate-id"
    headers = {
        "x-api-key": api_key
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("order_id")
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to generate order ID")

# Endpoint para processar o pedido
@app.post("/order", response_model=OrderResponse)
async def create_order(order_request: OrderRequest, x_api_key: str = Header(...)):
    if order_request.broth not in broths:
        raise HTTPException(status_code=400, detail="Invalid broth selection")
    
    if order_request.protein not in proteins:
        raise HTTPException(status_code=400, detail="Invalid protein selection")
    
    order_id = generate_order_id(x_api_key)
    
    return OrderResponse(order_id=order_id, message="Order successfully created")

# Comando para rodar a aplicação
# uvicorn main:app --reload
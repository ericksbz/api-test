from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import requests

app = FastAPI()

# Dados estáticos de exemplo para caldos e proteínas
broths = ["Shoyu", "Miso", "Tonkotsu", "Shio"]
proteins = ["Chicken", "Pork", "Beef", "Tofu"]
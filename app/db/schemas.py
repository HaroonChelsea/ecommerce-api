from pydantic import BaseModel
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    category: str
    price: float


class InventoryCreate(BaseModel):
    product_id: int
    stock_level: int


class SaleCreate(BaseModel):
    product_id: int
    quantity: int
    total_amount: float

# schemas/order.py
from pydantic import BaseModel
from datetime import datetime
from .user import User
from .product import Product

class OrderBase(BaseModel):
    user_id: int
    product_id: int
    total_price: float

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    created_at: datetime
    status: str
    user: User

product: Product
class Config:
    from_attributes = True  # 之前是 orm_mode = True
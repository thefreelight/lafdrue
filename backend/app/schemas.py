# app/schemas.py

from pydantic import BaseModel
from typing import Optional

# 用户模型
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_vip: bool
    is_agent: bool

    class Config:
        orm_mode = True

# 商品模型
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# 订单模型
class OrderBase(BaseModel):
    user_id: int
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    total_price: float
    status: str

    class Config:
        orm_mode = True

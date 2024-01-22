from pydantic import BaseModel,EmailStr
from typing import List

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

class OrderCreateSchema(BaseModel):
    user_email: EmailStr  # 使用 EmailStr 来确保邮箱格式正确
    items: List[OrderItemSchema]

class OrderSchema(OrderCreateSchema):
    id: int
    total_amount: float

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class OrderItemSchema(BaseModel):
    product_id: int
    product_name: str
    shipping_method: str
    quantity: int
    price: float

class OrderCreateSchema(BaseModel):
    user_email: EmailStr
    role: str
    payment_method: str
    client_ip: str
    handling_fee: Optional[float] = None
    card_info: Optional[str] = None
    items: List[OrderItemSchema]
    total_amount: float


class OrderSchema(OrderCreateSchema):
    id: int
    order_number: str
    order_time: datetime
    payment_status: str
    shipping_status: str

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True
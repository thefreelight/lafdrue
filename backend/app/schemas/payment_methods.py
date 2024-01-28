from pydantic import BaseModel, Json
from typing import Optional

class PaymentMethodBase(BaseModel):
    type: str
    merchant_id: Optional[str]
    secret_key: Optional[str]
    payment_gateway: Optional[str]
    name:Optional[str]

class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodRead(PaymentMethodBase):
    id: int

class PaymentMethodUpdate(BaseModel):
    type: Optional[str]
    merchant_id: Optional[str]
    secret_key: Optional[str]
    payment_gateway: Optional[str]
    name:Optional[str]


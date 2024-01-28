from pydantic import BaseModel

class PaymentRequest(BaseModel):
    method_id: int
    amount: float
    currency: str

class PaymentResponse(BaseModel):
    status: str
    transaction_id: str
    message: str

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True
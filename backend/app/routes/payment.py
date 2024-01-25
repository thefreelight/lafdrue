from fastapi import APIRouter
from ..services.payment import PaymentService
from ..schemas.payment import PaymentRequest, PaymentResponse

router = APIRouter()

@router.post("/payments/", response_model=PaymentResponse)
async def create_payment(payment_request: PaymentRequest):
    payment_service = PaymentService()
    return payment_service.process_payment(payment_request)

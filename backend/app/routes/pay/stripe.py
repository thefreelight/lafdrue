# 例如，使用 Stripe 的示例
# routes/payment.py
from fastapi import APIRouter, Depends, HTTPException, Body
from stripe import StripeError
import stripe

router = APIRouter()


@router.post("/pay")
def create_payment(amount: int = Body(...), token: str = Body(...)):
    try:
        stripe.api_key = "your_stripe_secret_key"

        charge = stripe.Charge.create(
            amount=amount,
            currency="usd",
            source=token,
            description="Charge for product"
        )
        return {"status": "success", "charge": charge}
    except StripeError as e:
        raise HTTPException(status_code=400, detail=str(e))

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.payment_methods import PaymentMethodCreate, PaymentMethodRead, PaymentMethodUpdate
from ..services.payment_methods import create_payment_method, get_payment_method, update_payment_method,get_all_payment_methods_service
from ..services.payments.payment_factory import PaymentFactory
from ..dependencies.database import get_db
from typing import List


router = APIRouter()

@router.post("/payment_methods/", response_model=PaymentMethodRead)
def create_payment_method_endpoint(payment_method: PaymentMethodCreate, db: Session = Depends(get_db)):
    return create_payment_method(db, payment_method)

@router.get("/payment_methods/{payment_method_id}", response_model=PaymentMethodRead)
def get_payment_method_endpoint(payment_method_id: int, db: Session = Depends(get_db)):
    db_payment_method = get_payment_method(db, payment_method_id)
    if db_payment_method is None:
        raise HTTPException(status_code=404, detail="Payment method not found")
    return db_payment_method

@router.put("/payment_methods/{payment_method_id}", response_model=PaymentMethodRead)
def update_payment_method_endpoint(payment_method_id: int, payment_method: PaymentMethodUpdate, db: Session = Depends(get_db)):
    return update_payment_method(db, payment_method_id, payment_method)

@router.get("/payment_methods/", response_model=List[PaymentMethodRead])
def get_all_payment_methods(db: Session = Depends(get_db)):
    return get_all_payment_methods_service(db)


@router.post("/payment_methods/create_payment_url")
async def create_payment_url_endpoint(payment_method: str, order_info: dict):
    payment_processor = PaymentFactory.get_processor(payment_method)
    if not payment_processor:
        raise HTTPException(status_code=404, detail="Payment processor not found")

    payment_url = payment_processor.create_payment_url(order_info)
    if not payment_url:
        raise HTTPException(status_code=500, detail="Failed to create payment URL")

    return {"payment_url": payment_url}
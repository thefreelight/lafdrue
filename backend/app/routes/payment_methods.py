from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.payment_methods import PaymentMethodCreate, PaymentMethodRead, PaymentMethodUpdate
from ..services.payment_methods import create_payment_method, get_payment_method, update_payment_method
from ..dependencies.database import get_db

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

from sqlalchemy.orm import Session
from ..models.payment_methods import PaymentMethod
from ..schemas.payment_methods import PaymentMethodCreate, PaymentMethodUpdate

def create_payment_method(db: Session, payment_method: PaymentMethodCreate):
    db_payment_method = PaymentMethod(**payment_method.dict())
    db.add(db_payment_method)
    db.commit()
    db.refresh(db_payment_method)
    return db_payment_method

def get_payment_method(db: Session, payment_method_id: int):
    return db.query(PaymentMethod).filter(PaymentMethod.id == payment_method_id).first()

def update_payment_method(db: Session, payment_method_id: int, payment_method: PaymentMethodUpdate):
    db_payment_method = db.query(PaymentMethod).filter(PaymentMethod.id == payment_method_id).first()
    if db_payment_method:
        update_data = payment_method.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_payment_method, key, value)
        db.commit()
        db.refresh(db_payment_method)
    return db_payment_method


def get_all_payment_methods_service(db: Session):
    payment_methods = db.query(PaymentMethod).all()
    return payment_methods
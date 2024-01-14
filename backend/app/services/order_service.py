from sqlalchemy.orm import Session
from ..models.order import Order
from ..services.referral_service import process_referral_order

def process_order(db: Session, order_data: dict, referral_code: str = None):
    order = Order(**order_data)
    db.add(order)
    db.commit()

    if referral_code:
        process_referral_order(db, order.total_amount, referral_code)

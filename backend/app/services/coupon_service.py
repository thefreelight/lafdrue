from datetime import datetime, timedelta
from ..models.coupon import Coupon
from sqlalchemy.orm import Session

def create_welcome_coupon(db: Session, user_id: int):
    welcome_coupon = Coupon(
        user_id=user_id,
        code="WELCOME10",
        discount=10.0,  # 10% 折扣
        valid_from=datetime.utcnow(),
        valid_to=datetime.utcnow() + timedelta(days=30)  # 有效期30天
    )
    db.add(welcome_coupon)
    db.commit()

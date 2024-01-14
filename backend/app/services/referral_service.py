
#### B. 推荐返利逻辑


from ..models.user import User
from sqlalchemy.orm import Session

def process_referral_order(db: Session, order_amount: float, referral_code: str):
    referrer = db.query(User).filter(User.referral_code == referral_code).first()
    if referrer:
        referrer.balance += calculate_referral_bonus(order_amount)  # 计算返利金额
        db.commit()

def calculate_referral_bonus(order_amount: float) -> float:
    return order_amount * 0.05  # 假设返利为订单金额的5%

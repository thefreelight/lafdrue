# ...其他代码...
from ..models.user import User
from ..services.coupon_service import create_welcome_coupon

def register_new_user(db: Session, user_data: dict) -> User:
    new_user = User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    if new_user.is_new_user:
        create_welcome_coupon(db, new_user.id)
    return new_user

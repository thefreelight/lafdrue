# crud/user.py
from sqlalchemy.orm import Session
from ..models.user import User, MembershipLevel
from ..schemas.user import UserCreate, MembershipLevelCreate,UserUpdate
from passlib.context import CryptContext

# 创建密码上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    """创建用户，并将密码哈希存储"""
    hashed_password = pwd_context.hash(user.password)  # 直接在这里哈希密码
    db_user = User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        return None
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()


def get_membership_level(db: Session, level_id: int):
    return db.query(MembershipLevel).filter(MembershipLevel.id == level_id).first()

def get_membership_levels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MembershipLevel).offset(skip).limit(limit).all()

def create_membership_level(db: Session, membership_level: MembershipLevelCreate):
    db_membership_level = MembershipLevel(**membership_level.dict())
    db.add(db_membership_level)
    db.commit()
    db.refresh(db_membership_level)
    return db_membership_level

# In services/user.py

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def recharge_user(db: Session, user_id: int, balance: float, commission: float):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    user.balance += balance
    user.commission += commission
    db.commit()
    return user
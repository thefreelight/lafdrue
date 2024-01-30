# crud/user.py
from sqlalchemy.orm import Session
from ..models.user import User, MembershipLevel
from ..schemas.user import UserCreate, MembershipLevelCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"  # Here you should use a proper hashing function
    db_user = User(email=user.email, username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

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

# ... 更多CRUD操作

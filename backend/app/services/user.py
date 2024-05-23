# crud/user.py
from sqlalchemy.orm import Session
from ..models.user import User, MembershipLevel
from ..schemas.user import UserCreate, MembershipLevelCreate,UserUpdate,MembershipLevelUpdate,UserQuery
from passlib.context import CryptContext

# 创建密码上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_membership_level(db: Session, membership_level: MembershipLevelCreate):
    db_membership_level = MembershipLevel(**membership_level.dict())
    db.add(db_membership_level)
    db.commit()
    db.refresh(db_membership_level)
    return db_membership_level

def get_membership_level(db: Session, membership_level_id: int):
    return db.query(MembershipLevel).filter(MembershipLevel.id == membership_level_id).first()

def get_membership_levels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MembershipLevel).offset(skip).limit(limit).all()

def update_membership_level(db: Session, membership_level_id: int, membership_level: MembershipLevelUpdate):
    db_membership_level = db.query(MembershipLevel).filter(MembershipLevel.id == membership_level_id).first()
    if db_membership_level is None:
        return None
    for var, value in vars(membership_level).items():
        setattr(db_membership_level, var, value) if value else None
    db.commit()
    db.refresh(db_membership_level)
    return db_membership_level

def delete_membership_level(db: Session, membership_level_id: int):
    db_membership_level = db.query(MembershipLevel).filter(MembershipLevel.id == membership_level_id).first()
    if db_membership_level is None:
        return None
    db.delete(db_membership_level)
    db.commit()
    return db_membership_level

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, query: UserQuery, skip: int = 0, limit: int = 10):
    # 初始化查询
    q = db.query(User)

    # 应用过滤条件
    if query.id:
        q = q.filter(User.id == query.id)
    if query.username:
        q = q.filter(User.username.contains(query.username))
    if query.email:
        q = q.filter(User.email.contains(query.email))
    if query.membership_level_id:
        q = q.filter(User.membership_level_id == query.membership_level_id)
    if query.is_agent is not None:
        q = q.filter(User.is_agent == query.is_agent)
    if query.balance is not None:
        q = q.filter(User.balance == query.balance)
    if query.commission is not None:
        q = q.filter(User.commission == query.commission)
    if query.referral_code:
        q = q.filter(User.referral_code.contains(query.referral_code))
    if query.is_active is not None:
        q = q.filter(User.is_active == query.is_active)

    return q

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
        raise HTTPException(status_code=404, detail="User not found")  # 如果用户不存在，抛出异常

    user_data = user.dict(exclude_unset=True)

    # 特别处理密码字段
    if 'password' in user_data and user_data['password']:
        hashed_password = pwd_context.hash(user_data['password'])
        db_user.hashed_password = hashed_password  # 确保数据库模型中的字段是 `hashed_password`

    # 更新其他字段
    for key, value in user_data.items():
        if key != 'password':  # 跳过密码字段，因为已经处理
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()


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
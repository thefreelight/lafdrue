# routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
# 假设这是你的 SQLAlchemy 模型
from ..models.user import User as DBUser
# 假设这是你的 Pydantic 模型
from ..schemas.user import User as SchemaUser
from ..schemas.user import UserCreate, User, MembershipLevelCreate, MembershipLevel,UserUpdate,Recharge
from ..services.user import create_user, get_user, get_users, create_membership_level, get_membership_levels,get_user_by_username,update_user,delete_user,recharge_user

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    # Check if a user with the provided username already exists.
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=Page[SchemaUser])
async def read_users(db: Session = Depends(get_db)):
    # 直接使用 SQLAlchemy 的 Query 对象
    query = db.query(DBUser)  # 假设 DBUser 是你的 SQLAlchemy 模型
    return paginate(query)


@router.put("/users/{user_id}", response_model=User)
def update_user_endpoint(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/users/{user_id}", response_model=dict)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user_id=user_id)
    return {"detail": "User deleted successfully"}

@router.post("/recharge/", response_model=User)
def recharge_user_endpoint(recharge: Recharge, db: Session = Depends(get_db)):
    try:
        user = recharge_user(db=db, user_id=recharge.user_id, balance=recharge.balance, commission=recharge.commission)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/membership_levels/", response_model=MembershipLevel)
def create_membership_level_endpoint(membership_level: MembershipLevelCreate, db: Session = Depends(get_db)):
    return create_membership_level(db=db, membership_level=membership_level)

@router.get("/membership_levels/{level_id}", response_model=MembershipLevel)
def read_membership_level(level_id: int, db: Session = Depends(get_db)):
    membership_level = get_membership_level(db, level_id=level_id)
    if membership_level is None:
        raise HTTPException(status_code=404, detail="Membership level not found")
    return membership_level

@router.get("/membership_levels/", response_model=list[MembershipLevel])
def read_membership_levels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    levels = get_membership_levels(db, skip=skip, limit=limit)
    return levels


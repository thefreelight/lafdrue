# routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
# 假设这是你的 SQLAlchemy 模型
from ..models.user import User as DBUser,MembershipLevel as DBMembershipLevel
# 假设这是你的 Pydantic 模型
from ..schemas.user import (
    UserCreate, User, MembershipLevelCreate, MembershipLevel,
    UserUpdate, MembershipLevelUpdate, Recharge,UserQuery
)
from ..services.user import (
    create_user, get_user, get_users, create_membership_level,
    get_membership_levels, get_membership_level, update_membership_level,
    delete_membership_level, get_user_by_username, update_user, delete_user, recharge_user
)

router = APIRouter()

@router.post("/membership_levels/", response_model=MembershipLevel, status_code=201)
def create_membership_endpoint(membership_level: MembershipLevelCreate, db: Session = Depends(get_db)):
    return create_membership_level(db=db, membership_level=membership_level)

@router.get("/membership_levels/{membership_level_id}", response_model=MembershipLevel)
def read_membership_endpoint(membership_level_id: int, db: Session = Depends(get_db)):
    membership_level = get_membership_level(db=db, membership_level_id=membership_level_id)
    if not membership_level:
        raise HTTPException(status_code=404, detail="Membership level not found")
    return membership_level

@router.get("/membership_levels/", response_model=Page[MembershipLevel])
def read_memberships_endpoint(db: Session = Depends(get_db)):
    return paginate(db.query(DBMembershipLevel))

@router.put("/membership_levels/{membership_level_id}", response_model=MembershipLevel)
def update_membership_endpoint(membership_level_id: int, membership_level: MembershipLevelUpdate, db: Session = Depends(get_db)):
    updated_membership_level = update_membership_level(db=db, membership_level_id=membership_level_id, membership_level=membership_level)
    if not updated_membership_level:
        raise HTTPException(status_code=404, detail="Membership level not found")
    return updated_membership_level

@router.delete("/membership_levels/{membership_level_id}", response_model=dict)
def delete_membership_endpoint(membership_level_id: int, db: Session = Depends(get_db)):
    membership_level = delete_membership_level(db=db, membership_level_id=membership_level_id)
    if not membership_level:
        raise HTTPException(status_code=404, detail="Membership level not found")
    return {"detail": "Membership level deleted successfully"}


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

@router.get("/users/", response_model=Page[UserQuery])
def read_users(
    query: UserQuery = Depends(),  # 使用依赖注入获取查询参数
    db: Session = Depends(get_db)
):
    query_obj = get_users(db=db, query=query)  # 获取查询对象
    return paginate(query_obj)  # 使用 paginate 函数应用分页


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



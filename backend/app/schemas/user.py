# schemas/user.py
from pydantic import BaseModel
from typing import Optional,List
from fastapi import Query

class MembershipLevelBase(BaseModel):
    name: str
    benefits: Optional[str] = None
    icon: Optional[str] = None
    points_required: int
    discount: float


class MembershipLevelCreate(MembershipLevelBase):
    pass

class MembershipLevelUpdate(BaseModel):
    name: Optional[str] = None
    benefits: Optional[str] = None
    icon: Optional[str] = None
    points_required: Optional[int] = None
    discount: Optional[float] = None

class MembershipLevel(MembershipLevelBase):
    id: int
    users: List[int] = []

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    referral_code: Optional[str] = None
    membership_level: Optional[MembershipLevel] = None
    is_agent: Optional[bool] = None
    is_active: Optional[bool] = None

class UserQuery(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    membership_level_id: Optional[int] = None
    is_agent: Optional[bool] = None
    balance: Optional[float] = None
    commission: Optional[float] = None
    referral_code: Optional[str] = None
    is_active: Optional[bool] = None


class Recharge(BaseModel):
    user_id: int
    balance: float
    commission: float

class User(UserBase):
    id: int
    membership_level: Optional[MembershipLevel] = None
    is_agent: bool
    balance: float
    commission: float
    referral_code: Optional[str] = None
    is_active: bool


    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

# schemas/user.py
from pydantic import BaseModel
from typing import Optional

class MembershipLevelBase(BaseModel):
    name: str
    benefits: str
    icon: str
    points_required: int
    discount: float

class MembershipLevelCreate(MembershipLevelBase):
    pass

class MembershipLevel(MembershipLevelBase):
    id: int

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

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

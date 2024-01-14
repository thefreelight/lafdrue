# schemas/user.py
from pydantic import BaseModel
from .role import Role

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: Role


    class Config:
        from_attributes = True  # 之前是 orm_mode = True

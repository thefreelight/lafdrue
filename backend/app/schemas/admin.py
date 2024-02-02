# schemas/admin.py
from pydantic import BaseModel
from typing import Optional


class AdminRoleBase(BaseModel):
    name: str
    permissions: str

class AdminRoleCreate(AdminRoleBase):
    pass

class AdminRoleUpdate(BaseModel):
    name: Optional[str] = None
    permissions: Optional[str] = None

class AdminRole(AdminRoleBase):
    id: int

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True


class AdminBase(BaseModel):
    username: str
    email: str

class AdminCreate(AdminBase):
    password: str
    role_id: int

class Admin(AdminBase):
    id: int
    is_active: bool
    role: Optional[AdminRole] = None  # Assuming AdminRole is optional in Admin

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True


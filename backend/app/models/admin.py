# models/admin.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AdminRole(Base):
    __tablename__ = 'admin_roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    permissions = Column(String(255))  # 可以是一个权限列表的JSON字符串

    admins = relationship("Admin", back_populates="role")

class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    role_id = Column(Integer, ForeignKey('admin_roles.id'))
    role = relationship("AdminRole", back_populates="admins")
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)


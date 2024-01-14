# models/user.py
from sqlalchemy import Column, Integer, String,ForeignKey,Boolean,Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role")
    is_new_user = Column(Boolean, default=True)  # 新用户标识
    balance= Column(Numeric(10, 2), default=0)  # 用户余额，用于返利
    referral_code = Column(String(50), unique=True, index=True)
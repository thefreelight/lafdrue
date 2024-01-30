# models/user.py
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MembershipLevel(Base):
    __tablename__ = 'membership_levels'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    benefits = Column(String(255))
    icon = Column(String(255))
    points_required = Column(Integer)
    discount = Column(Float)
    users = relationship("User", back_populates="membership_level")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    membership_level_id = Column(Integer, ForeignKey('membership_levels.id'))
    membership_level = relationship("MembershipLevel", back_populates="users")
    is_agent = Column(Boolean, default=False)
    email = Column(String(100), unique=True, index=True)
    balance = Column(Float, default=0.0)
    commission = Column(Float, default=0.0)
    referral_code = Column(String(50), index=True)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String(100))

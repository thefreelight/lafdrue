from sqlalchemy import Column, Integer, String,Float
from ..database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    discount = Column(Float, default=0)  # 折扣百分比

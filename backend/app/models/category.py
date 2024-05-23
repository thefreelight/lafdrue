from sqlalchemy import Column, Integer, String,Boolean
from ..dependencies.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    is_active = Column(Boolean, default=True)  # 表示状态，是否激活
    display = Column(Boolean, default=True)  # 表示是否在前端显示
    order = Column(Integer, default=0)  # 用于排序的数字
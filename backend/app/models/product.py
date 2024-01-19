from sqlalchemy import Column, Integer, String, Float, Text
from ..dependencies.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # 指定长度为 255
    category = Column(String(255), index=True)  # 指定长度为 255
    price = Column(Float)
    description = Column(Text)  # Text 类型不需要指定长度
    image_url = Column(String(500), index=True)  # 指定长度为 255

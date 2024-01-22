from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text,DateTime,Boolean
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from sqlalchemy.sql import func



# 商品模型
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, index=True)
    name = Column(String(255), index=True)
    brand = Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.id'))
    price = Column(Float)
    stock = Column(Integer, default=0)
    description = Column(Text)
    image_url = Column(String(500))
    status = Column(String(50))
    ratings = Column(Float, default=0.0)
    is_featured = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # 确保添加了这个关系属性并且设置了正确的反向关系
    order_items = relationship('OrderItem', back_populates='product')

    category = relationship("Category")


from sqlalchemy import Column, Float, String, Integer, ForeignKey, DateTime,Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import random
from ..dependencies.database import Base
from enum import Enum
from sqlalchemy.types import Enum as SqlEnum



class PaymentStatus(Enum):
    UNPAID = "未支付"
    PROCESSING = "正在处理"
    PAID = "已支付"
    FAILED = "支付失败"

class ShippingStatus(Enum):
    UNSENT = "未发货"
    PREPARING = "准备中"
    SENT = "已发货"
    DELIVERED = "已送达"


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(12), default=lambda: str(random.randint(100000000000, 999999999999)))
    user_email = Column(String(255), index=True)
    total_amount = Column(Float)
    role = Column(String(50))
    payment_method = Column(String(50))
    order_time = Column(DateTime, default=func.now())
    client_ip = Column(String(50))
    payment_status = Column(SqlEnum(PaymentStatus))
    shipping_status = Column(SqlEnum(ShippingStatus))
    handling_fee = Column(Float)
    card_info = Column(Text)
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    product_name = Column(String(255))
    shipping_method = Column(String(50))
    quantity = Column(Integer)
    price = Column(Float)
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")

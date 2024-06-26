from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base

from ..dependencies.database import Base

class PaymentMethod(Base):
    __tablename__ = 'payment_methods'
    id = Column(Integer, primary_key=True)
    name = Column(String(50)) #支付名称 支付宝，微信
    type = Column(String(50))  # 支付类型，如 扫码付
    merchant_id = Column(String(255))  # 通用商户ID
    secret_key = Column(String(255))  # 通用密钥
    payment_gateway = Column(String(255))  # 通用支付网关
    payment_method = Column(String(50))  # 新添加的支付方式字段


    # 其他通用字段，如创建时间、更新时间等

# 您可以根据需要添加方法和关系




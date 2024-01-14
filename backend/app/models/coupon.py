# models/coupon.py
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from ..database import Base
import datetime


class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount = Column(Float)
    valid_from = Column(DateTime, default=datetime.datetime.utcnow)
    valid_to = Column(DateTime)


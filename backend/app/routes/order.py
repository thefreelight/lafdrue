# routes/order.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.order import OrderCreate, Order
from ..services.crud_order import create_order,update_order_status
from ..database import SessionLocal
from ..models.order import OrderStatus

router = APIRouter()

@router.post("/orders/", response_model=Order)
def create_order_view(order: OrderCreate, db: Session = Depends(SessionLocal)):
    return create_order(db=db, order=order)

# 添加更多路由，如获取订单列表、获取特定订单、更新和删除订单
@router.put("/orders/{order_id}/status")
def update_order_status_view(order_id: int, status: OrderStatus, db: Session = Depends(SessionLocal)):
    return update_order_status(db, order_id, status)
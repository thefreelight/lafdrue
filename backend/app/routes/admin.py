from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.order import Order
from ..database import SessionLocal
from ..dependencies.jwt_dependency import get_current_user

router = APIRouter()

@router.get("/admin/orders")
async def get_all_orders(db: Session = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    if current_user.role.name != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    # 添加获取所有订单的逻辑
    return {"orders": "All orders"}

@router.get("/admin/products")
async def get_all_products(db: Session = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    if current_user.role.name != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    # 添加获取所有产品的逻辑
    return {"products": "All products"}

@router.get("/admin/orders")
async def get_all_orders(db: Session = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    orders = db.query(Order).all()
    return orders

@router.put("/admin/orders/{order_id}")
async def update_order_status(order_id: int, new_status: str, db: Session = Depends(SessionLocal), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Insufficient permissions")
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = new_status
    db.commit()
    return {"message": "Order status updated successfully"}
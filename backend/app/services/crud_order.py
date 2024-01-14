
### 3. 订单 CRUD 操作

# services/crud_order.py
from sqlalchemy.orm import Session
from ..models.order import Order
from ..schemas.order import OrderCreate
from ..models.order import Order, OrderStatus
from .notification_service import send_email_notification


def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# 添加更多操作，如获取订单、更新订单状态、删除订单等
def update_order_status(db: Session, order_id: int, status: OrderStatus):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order:
        if order.status != OrderStatus.COMPLETED and status == OrderStatus.COMPLETED:
            # 发送订单完成通知
            send_email_notification(
                "Order Completed",
                f"Your order {order_id} is completed.",
                "customer@example.com"
            )

        order.status = status
        db.commit()
        return order
    else:
        raise Exception("Order not found")

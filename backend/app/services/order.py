from sqlalchemy.orm import Session
from ..models.order import Order, OrderItem
from ..schemas.order import OrderCreateSchema  # 这里直接从 schemas.order 导入 OrderCreateSchema

def create_order(db: Session, order_create: OrderCreateSchema):
    # 创建订单实例
    total_amount = sum(item.quantity * item.price for item in order_create.items)
    print(order_create.items)
    order = Order(user_email=order_create.user_email, total_amount=total_amount)
    db.add(order)
    db.commit()
    # 创建订单项
    for item in order_create.items:
        db.add(OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, price=item.price))
    db.commit()
    return order

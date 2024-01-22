from sqlalchemy.orm import Session
from ..models.order import Order, OrderItem
from ..schemas.order import OrderCreateSchema


def create_order(db: Session, order_create: OrderCreateSchema):
    try:
        # 计算总金额
        total_amount = sum(item.quantity * item.price for item in order_create.items)

        # 创建订单实例
        order = Order(user_email=order_create.user_email, total_amount=total_amount)
        db.add(order)
        db.flush()  # 使用 flush 来获取 order 的 ID，但不提交事务

        # 创建订单项
        for item_data in order_create.items:
            item = OrderItem(
                order_id=order.id,
                product_id=item_data.product_id,
                quantity=item_data.quantity,
                price=item_data.price
            )
            db.add(item)

        # 提交所有更改
        db.commit()
        return order
    except Exception as e:
        # 打印错误信息
        print(f"Error creating order: {e}")
        # 回滚事务
        db.rollback()
        # 这里可以抛出更具体的异常或返回错误信息
        raise e

from sqlalchemy.orm import Session
from ..models.order import Order, OrderItem,PaymentStatus,ShippingStatus
from ..schemas.order import OrderCreateSchema

def create_order(db: Session, order_create: OrderCreateSchema):
    try:
        # 使用前端提供的总金额
        total_amount = order_create.total_amount

        # 创建订单实例，初始化支付状态和发货状态
        order = Order(
            user_email=order_create.user_email,
            role=order_create.role,
            payment_method=order_create.payment_method,
            client_ip=order_create.client_ip,
            payment_status= PaymentStatus.UNPAID,
            shipping_status= ShippingStatus.UNSENT,
            total_amount=total_amount,
            handling_fee=order_create.handling_fee,  # 如果存在
            card_info=order_create.card_info  # 如果存在
        )
        db.add(order)
        db.flush()  # 使用 flush 来获取 order 的 ID，但不提交事务

        # 创建订单项
        for item_data in order_create.items:
            item = OrderItem(
                order_id=order.id,
                product_id=item_data.product_id,
                product_name=item_data.product_name,  # 确保 OrderItem 有此字段
                shipping_method=item_data.shipping_method,  # 确保 OrderItem 有此字段
                quantity=item_data.quantity,
                price=item_data.price
            )
            db.add(item)

        # 提交所有更改
        db.commit()
        return order
    except Exception as e:
        print(f"Error creating order: {e}")
        db.rollback()
        raise e

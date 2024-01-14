# services/crud_product.py
from sqlalchemy.orm import Session
from ..models.product import Product
from ..schemas.product import ProductCreate
from ..services.notification_service import send_email_notification


def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 添加更多操作，如获取商品、更新商品、删除商品等
# services/crud_product.py
from sqlalchemy.orm import Session
from models.product import Product
from services.notification_service import send_email_notification

def decrease_product_stock(db: Session, product_id: int, quantity: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        if product.stock >= quantity:
            product.stock -= quantity
            db.commit()

            # 库存低于阈值时发送通知
            if product.stock < 10:  # 示例阈值
                send_email_notification(
                    "Low Stock Warning",
                    f"Product {product_id} is low on stock.",
                    "admin@example.com"
                )
            return product
        else:
            raise Exception("Insufficient stock")
    else:
        raise Exception("Product not found")

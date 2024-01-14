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



def check_and_notify_low_stock(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product and product.stock < 10:  # 假设阈值为10
        send_email_notification(
            "Low Stock Warning",
            f"Product {product.name} is low on stock.",
            "admin@example.com"  # 管理员邮箱
        )
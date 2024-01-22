# product.py
from sqlalchemy.orm import Session
from ..models.product import Product as DBProduct
from ..schemas.product import ProductCreate

def get_product(db: Session, product_id: int):
    return db.query(DBProduct).filter(DBProduct.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DBProduct).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = DBProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
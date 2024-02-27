# product.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.product import Product
from ..schemas.product import ProductCreate,ProductQuery

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, query: ProductQuery, skip: int = 0, limit: int = 10):
    # Initialize the query
    q = db.query(Product)

    # Apply filtering conditions
    if query.category_id:
        q = q.filter(Product.category_id == query.category_id)
    if query.name:
        q = q.filter(Product.name.contains(query.name))
    if query.status:
        q = q.filter(Product.status == query.status)

    return q

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Update a product
def update_product(db: Session, product_id: int, update_data: dict):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product

# Delete a product
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    return {"ok": True}

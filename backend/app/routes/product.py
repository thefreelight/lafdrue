from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.product import get_products, get_product, create_product
from ..schemas.product import ProductCreate, Product
from ..dependencies.database import get_db
from typing import List

router = APIRouter()

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/products/", response_model=List[Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = get_products(db, skip=skip, limit=limit)
    return products

@router.post("/products/", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

# ...其他端点

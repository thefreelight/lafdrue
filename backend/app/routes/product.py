# product.py
from fastapi import APIRouter, Depends,Query
from sqlalchemy.orm import Session
from ..services import product as product_service
from ..dependencies.database import get_db
from ..schemas.product import Product, ProductCreate
from typing import List


router = APIRouter()

@router.get("/products/", response_model=List[Product])
def read_products(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    return product_service.get_products(db, skip=skip, limit=limit)

@router.post("/products/", response_model=Product)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product=product)




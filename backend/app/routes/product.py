# routes/product.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.product import ProductCreate, Product
from ..services.crud_product import create_product,decrease_product_stock
from ..database import SessionLocal

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_product_view(product: ProductCreate, db: Session = Depends(SessionLocal)):
    return create_product(db=db, product=product)

# 添加更多路由，如获取商品列表、获取特定商品、更新和删除商品
@router.post("/products/{product_id}/decrease_stock")
def decrease_stock(product_id: int, quantity: int, db: Session = Depends(SessionLocal)):
    return decrease_product_stock(db, product_id, quantity)
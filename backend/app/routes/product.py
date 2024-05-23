from fastapi import APIRouter, Depends, HTTPException,status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..services.product import get_products, get_product, create_product,update_product,delete_product
from ..schemas.product import ProductCreate, Product,ProductQuery
from ..dependencies.database import get_db
from typing import List

router = APIRouter()

@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/products/", response_model=Page[Product])
def read_products(
    query: ProductQuery = Depends(),  # Use dependency injection to obtain query parameters
    db: Session = Depends(get_db)  # Use dependency injection to obtain database session
):
    query_obj = get_products(db=db, query=query)  # Obtain query object using filters
    return paginate(query_obj)  # Apply pagination using the paginate function

@router.post("/products/", response_model=Product)
def create_product_endpoint(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)

@router.put("/products/{product_id}", response_model=Product)
def update_product_endpoint(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    return update_product(db=db, product_id=product_id, update_data=product.dict())

@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    delete_product(db=db, product_id=product_id)
    return {"ok": True}
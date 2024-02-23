from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..schemas.category import CategoryCreate, CategoryUpdate, Category,CategoryQuery
from ..dependencies.database import get_db
from ..services.category import (
    create_category, get_categories, get_category,
    update_category, delete_category
)

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category_view(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db=db, category=category)

@router.get("/categories/", response_model=Page[Category])
def get_categories_view(
    query: CategoryQuery = Depends(),  # 从请求中获取查询参数
    db: Session = Depends(get_db)
):
    categories_query = get_categories(db=db, query=query)
    return paginate(categories_query)

@router.get("/categories/{category_id}", response_model=Category)
def get_category_view(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/categories/{category_id}", response_model=Category)
def update_category_view(category_id: int, category: CategoryUpdate, db: Session = Depends(get_db)):
    updated_category = update_category(db=db, category_id=category_id, category=category)
    if updated_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@router.delete("/categories/{category_id}", response_model=Category)
def delete_category_view(category_id: int, db: Session = Depends(get_db)):
    category = delete_category(db=db, category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


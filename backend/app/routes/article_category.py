from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.article_category import (
    get_article_category,
    get_article_categories,
    create_article_category as create_article_category_service,
    update_article_category as update_article_category_service,
    delete_article_category as delete_article_category_service
)
from app.schemas.article_category import ArticleCategoryCreate, ArticleCategoryUpdate, ArticleCategory
from app.dependencies.database import get_db
from typing import List

router = APIRouter()

@router.get("/article_categories/", response_model=List[ArticleCategory])
def read_article_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_article_categories(db, skip=skip, limit=limit)

@router.get("/article_categories/{category_id}", response_model=ArticleCategory)
def read_article_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_article_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return db_category

@router.post("/article_categories/", response_model=ArticleCategory)
def create_article_category(category: ArticleCategoryCreate, db: Session = Depends(get_db)):
    return create_article_category_service(db=db, category=category)

@router.put("/article_categories/{category_id}", response_model=ArticleCategory)
def update_article_category(category_id: int, category: ArticleCategoryUpdate, db: Session = Depends(get_db)):
    db_category = update_article_category_service(db=db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return db_category

@router.delete("/article_categories/{category_id}", response_model=ArticleCategory)
def delete_article_category(category_id: int, db: Session = Depends(get_db)):
    db_category = delete_article_category_service(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return db_category

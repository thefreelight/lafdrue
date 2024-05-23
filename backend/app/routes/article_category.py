from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.article_category import ArticleCategory as DBArticleCategory
from ..schemas.article_category import ArticleCategoryCreate, ArticleCategoryUpdate, ArticleCategory
from ..services.article_category import (
    get_article_category, get_article_categories,
    create_article_category as create_article_category_service,
    update_article_category as update_article_category_service,
    delete_article_category as delete_article_category_service
)
from typing import List

router = APIRouter()

@router.post("/article-categories/", response_model=ArticleCategory, status_code=201)
def create_article_category(category: ArticleCategoryCreate, db: Session = Depends(get_db)):
    return create_article_category_service(db=db, category=category)

@router.get("/article-categories/{category_id}", response_model=ArticleCategory)
def read_article_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_article_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return db_category

@router.get("/article-categories/", response_model=Page[ArticleCategory])
def read_article_categories(db: Session = Depends(get_db)):
    return paginate(db.query(DBArticleCategory))

@router.put("/article-categories/{category_id}", response_model=ArticleCategory)
def update_article_category(category_id: int, category: ArticleCategoryUpdate, db: Session = Depends(get_db)):
    db_category = update_article_category_service(db=db, category_id=category_id, category=category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return db_category

@router.delete("/article-categories/{category_id}", response_model=dict)
def delete_article_category(category_id: int, db: Session = Depends(get_db)):
    db_category = delete_article_category_service(db=db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="ArticleCategory not found")
    return {"detail": "ArticleCategory deleted successfully"}

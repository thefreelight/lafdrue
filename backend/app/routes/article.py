from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from app.schemas.article import Article, ArticleCreate
from app.services.article import (
    create_article, get_article, get_articles, update_article, delete_article
)
from app.dependencies.database import get_db

router = APIRouter()

@router.post("/", response_model=Article, status_code=201)
def create_article_route(article: ArticleCreate, db: Session = Depends(get_db)):
    return create_article(db=db, article=article)

@router.get("/{article_id}", response_model=Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = get_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/", response_model=Page[Article])
def read_articles(db: Session = Depends(get_db)):
    return paginate(db.query(Article))

@router.put("/{article_id}", response_model=Article)
def update_article_route(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    updated_article = update_article(db=db, article_id=article_id, article=article)
    if not updated_article:
        raise HTTPException(status_code=404, detail="Article not found")
    return updated_article

@router.delete("/{article_id}", response_model=dict)
def delete_article_route(article_id: int, db: Session = Depends(get_db)):
    article = delete_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"detail": "Article deleted successfully"}

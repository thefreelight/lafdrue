from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.article import Article as DBArticle
from ..schemas.article import ArticleCreate, Article
from ..services.article import (
    create_article, get_article, get_articles, update_article, delete_article
)

router = APIRouter()

@router.post("/articles/", response_model=Article, status_code=201)
def create_article_route(article: ArticleCreate, db: Session = Depends(get_db)):
    return create_article(db=db, article=article)

@router.get("/articles/{article_id}", response_model=Article)
def read_article(article_id: int, db: Session = Depends(get_db)):
    article = get_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/articles/", response_model=Page[Article])
def read_articles(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return paginate(db.query(DBArticle).offset(skip).limit(limit))

@router.put("/articles/{article_id}", response_model=Article)
def update_article_route(article_id: int, article: ArticleCreate, db: Session = Depends(get_db)):
    updated_article = update_article(db=db, article_id=article_id, article=article)
    if not updated_article:
        raise HTTPException(status_code=404, detail="Article not found")
    return updated_article

@router.delete("/articles/{article_id}", response_model=dict)
def delete_article_route(article_id: int, db: Session = Depends(get_db)):
    article = delete_article(db=db, article_id=article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"detail": "Article deleted successfully"}

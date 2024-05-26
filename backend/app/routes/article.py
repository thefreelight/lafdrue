from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from typing import Optional
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
def read_articles(
        db: Session = Depends(get_db),
        skip: Optional[str] = Query("0"),
        limit: Optional[str] = Query("10"),
        category_id: Optional[int] = Query(None),
        language: Optional[str] = Query(None)
):
    try:
        skip = int(skip) if skip else 0
        limit = int(limit) if limit else 10
    except ValueError:
        raise HTTPException(status_code=422, detail="Query parameters 'skip' and 'limit' must be valid integers.")

    query = db.query(DBArticle)
    if category_id is not None:
        query = query.filter(DBArticle.category_id == category_id)
    if language is not None:
        query = query.filter(DBArticle.language == language)

    return paginate(query.offset(skip).limit(limit))


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

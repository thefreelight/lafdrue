from sqlalchemy.orm import Session
from ..models.article import Article as DBArticle
from ..schemas.article import ArticleCreate

def create_article(db: Session, article: ArticleCreate):
    db_article = DBArticle(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_article(db: Session, article_id: int):
    return db.query(DBArticle).filter(DBArticle.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 10, category_id: int = None, language: str = None):
    query = db.query(DBArticle)
    if category_id is not None:
        query = query.filter(DBArticle.category_id == category_id)
    if language is not None:
        query = query.filter(DBArticle.language == language)
    return query.offset(skip).limit(limit).all()

def update_article(db: Session, article_id: int, article: ArticleCreate):
    db_article = db.query(DBArticle).filter(DBArticle.id == article_id).first()
    if not db_article:
        return None
    for key, value in article.dict().items():
        setattr(db_article, key, value)
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = db.query(DBArticle).filter(DBArticle.id == article_id).first()
    if not db_article:
        return None
    db.delete(db_article)
    db.commit()
    return db_article

from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate

def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()

def create_article(db: Session, article: ArticleCreate):
    db_article = Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def update_article(db: Session, article_id: int, article: ArticleCreate):
    db_article = get_article(db, article_id)
    if not db_article:
        return None
    for var, value in vars(article).items():
        setattr(db_article, var, value) if value else None
    db.commit()
    db.refresh(db_article)
    return db_article

def delete_article(db: Session, article_id: int):
    db_article = get_article(db, article_id)
    if not db_article:
        return None
    db.delete(db_article)
    db.commit()
    return db_article

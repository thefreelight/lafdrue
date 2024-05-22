from sqlalchemy.orm import Session
from app.models.article_category import ArticleCategory
from app.schemas.article_category import ArticleCategoryCreate, ArticleCategoryUpdate

def get_article_category(db: Session, category_id: int):
    return db.query(ArticleCategory).filter(ArticleCategory.id == category_id).first()

def get_article_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ArticleCategory).offset(skip).limit(limit).all()

def create_article_category(db: Session, category: ArticleCategoryCreate):
    db_category = ArticleCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_article_category(db: Session, category_id: int, category: ArticleCategoryUpdate):
    db_category = get_article_category(db, category_id)
    if not db_category:
        return None
    for var, value in vars(category).items():
        if value is not None:
            setattr(db_category, var, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_article_category(db: Session, category_id: int):
    db_category = get_article_category(db, category_id)
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category

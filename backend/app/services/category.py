from sqlalchemy.orm import Session
from ..models.category import Category as DBCategory
from ..schemas.category import CategoryCreate

# 创建新的分类
def create_category(db: Session, category: CategoryCreate):
    db_category = DBCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# 获取所有分类
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DBCategory).offset(skip).limit(limit).all()

# 获取单个分类
def get_category(db: Session, category_id: int):
    return db.query(DBCategory).filter(DBCategory.id == category_id).first()

# 更新分类
def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = get_category(db, category_id)
    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)
    return db_category

# 删除分类
def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

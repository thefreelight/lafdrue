from sqlalchemy.orm import Session
from ..models.category import Category as DBCategory
from ..schemas.category import CategoryCreate,CategoryQuery

# 创建新的分类
def create_category(db: Session, category: CategoryCreate):
    db_category = DBCategory(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# 现在的get_categories函数使用paginate函数来创建分页响应

def get_categories(db: Session, query: CategoryQuery, skip: int = 0, limit: int = 10):
    q = db.query(DBCategory)  # Start with a query that gets all categories

    # Apply name filter if provided
    if query.name:
        q = q.filter(DBCategory.name.contains(query.name))

    # Apply skipping and limiting to the query

    return q


# 获取单个分类
def get_category(db: Session, category_id: int):
    return db.query(DBCategory).filter(DBCategory.id == category_id).first()

# 更新分类
# 更新分类的逻辑需要包含新的字段
def update_category(db: Session, category_id: int, category: CategoryCreate):
    db_category = get_category(db, category_id)
    if db_category:
        db_category.name = category.name
        db_category.is_active = category.is_active
        db_category.display = category.display
        db_category.order = category.order
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

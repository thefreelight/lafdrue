from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.category import Category as CategoryModel
from ..schemas.category import CategoryCreate, Category
from ..dependencies.database import get_db

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = CategoryModel(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    is_active: bool
    display: bool
    order: int

class Category(CategoryBase):
    id: int
    is_active: bool
    display: bool
    order: int

class CategoryQuery(BaseModel):
    name: Optional[str] = None


    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

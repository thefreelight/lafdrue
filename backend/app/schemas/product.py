from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from .category import Category

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    price: float
    stock: Optional[int] = 0
    description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None

class ProductCreate(ProductBase):
    category_id: int

class ProductQuery(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None

class Product(ProductBase):
    id: int
    sku: Optional[str] = None
    ratings: float
    is_featured: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    category: Category

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

# product.py
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    category: str
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True  # 替换原来的 orm_mode = True

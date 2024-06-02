from typing import Optional
from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    content: str
    author: Optional[str] = None  # 修改此处，author 字段允许为 None
    category_id: int
    language: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        from_attributes = True

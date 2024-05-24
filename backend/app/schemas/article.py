from pydantic import BaseModel
from typing import Optional

class ArticleBase(BaseModel):
    title: str
    content: str
    author: Optional[str] = None
    category_id: Optional[int] = None

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        from_attributes = True


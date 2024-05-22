from pydantic import BaseModel
from .article_category import ArticleCategory

class ArticleBase(BaseModel):
    title: str
    content: str
    category_id: int

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int
    category: ArticleCategory

    class Config:
        from_attributes = True

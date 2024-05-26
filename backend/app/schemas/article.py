from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    content: str
    author: str = None
    category_id: int
    language: str

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        from_attributes = True


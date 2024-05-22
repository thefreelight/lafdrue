from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class ArticleCategory(Base):
    __tablename__ = "article_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, unique=True)  # 指定长度

    articles = relationship("Article", back_populates="category")

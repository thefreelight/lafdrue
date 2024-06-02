from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text)
    author = Column(String(255), nullable=True, default="Unknown")  # 添加默认值
    category_id = Column(Integer, ForeignKey("article_categories.id"))
    category = relationship("ArticleCategory", back_populates="articles")
    language = Column(String(10), nullable=False)

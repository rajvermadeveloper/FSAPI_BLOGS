
from sqlalchemy import Column, Integer, String, DateTime,Text
from app.api.dependencies.database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(355), index=True)
    content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


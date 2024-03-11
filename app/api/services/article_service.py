from sqlalchemy.orm import Session
from models.article import Article

def create_article(db: Session, article_data: dict):
    db_article = Article(**article_data)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_article(article_id: int):
    pass

def update_article(article_id: int, article: Article):
    pass

def delete_article(article_id: int):
    pass
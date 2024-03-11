from fastapi import Depends,APIRouter
# from services import article_service
# from models.article import Article

router = APIRouter(prefix="/articles")
# from dependencies.authentication import get_current_user

@router.post("/")
async def create_article():
    pass

@router.get("/{article_id}")
async def get_article(article_id: int):
    pass

@router.put("/{article_id}")
async def update_article(article_id: int):
    pass

@router.delete("/{article_id}")
async def delete_article(article_id: int):
    pass
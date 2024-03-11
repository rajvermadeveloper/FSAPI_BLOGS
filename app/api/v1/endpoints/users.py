from fastapi import Depends,APIRouter,HTTPException
from app.api.services.user_service import create_user
from app.api.v1.schemas.user import UserCreate
from app.api.dependencies.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users")


@router.post("/")
async def create_new_user(user_data: UserCreate,db: Session = Depends(get_db)):
    user = create_user(db=db, user_data=user_data)
    if not user:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return {"message": "User created successfully"}


@router.get("/{article_id}")
async def get_user(article_id: int):
    pass

@router.put("/{article_id}")
async def update_user(article_id: int):
    pass

@router.delete("/{article_id}")
async def delete_user(article_id: int):
    pass
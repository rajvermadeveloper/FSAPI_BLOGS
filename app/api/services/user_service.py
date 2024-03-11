from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.api.models.user import User
from app.api.v1.schemas.user import UserCreate
from app.api.core.security import get_password_hash
from app.api.dependencies.database import SessionLocal
from app.api.core.security import get_password_hash

def create_user(db: Session, user_data: dict):
    hashed_password = get_password_hash(user_data.password)  # Assuming you have a function to hash passwords
    db_user = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
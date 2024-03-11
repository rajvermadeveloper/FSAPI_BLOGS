from fastapi import Depends, HTTPException, status
from core.config import SECRET_KEY
from utils.helpers import verify_password
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(username: str, password: str):
    pass

def get_current_user(token: str = Depends(oauth2_scheme)):
    pass
from datetime import datetime, timedelta
from typing import Union, Any, Coroutine

from fastapi import APIRouter


from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
import jwt


from kaiyuanshe_werobot.crud import user as crud_user
from kaiyuanshe_werobot.schemas import auth, users
from kaiyuanshe_werobot.schemas.users import User
from kaiyuanshe_werobot.util import verify_password

router = APIRouter()


ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


@router.post("/token", response_model=auth.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username, "user_id": user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def authenticate_user(username: str, password: str) -> Coroutine[Any, Any, User]:
    user: users.User = await crud_user.get_user(username=username, user_id=0)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user




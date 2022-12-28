from fastapi import APIRouter

from kaiyuanshe_werobot.api.endpoints import (
    user, oauth
)

api_router = APIRouter()
api_router.include_router(user.router, tags=["user"], prefix="/user")
api_router.include_router(oauth.router, tags=["oauth"], prefix="/oauth")

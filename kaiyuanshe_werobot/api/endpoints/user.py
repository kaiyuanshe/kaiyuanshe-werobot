from typing import List, Union

from fastapi import APIRouter

from kaiyuanshe_werobot import models
from kaiyuanshe_werobot.schemas.users import UserIn, User
from kaiyuanshe_werobot.db.database import database
from kaiyuanshe_werobot import crud

router = APIRouter()


@router.post("/create", response_model=Union[int, None])
async def create_user(user: UserIn):
    record_id = await crud.user.create_user(user)
    return record_id


@router.get("/users/", response_model=List[User])
async def all_users():
    query = models.users.select()
    return await database.fetch_all(query)


@router.get("/users/:user_id", response_model=Union[User, None])
async def get_user(user_id: int):
    user = await crud.user.get_user(user_id=user_id, username="")
    return user

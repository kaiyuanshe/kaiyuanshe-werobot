from typing import Union

from kaiyuanshe_werobot import models
from kaiyuanshe_werobot.schemas.users import UserIn, User
from kaiyuanshe_werobot.db.database import database
from kaiyuanshe_werobot.util import hash_password

import pymysql


async def create_user(user: UserIn) -> Union[int, None]:
    try:
        user.hashed_password = hash_password(user.hashed_password)
        query = models.users.insert().values(username=user.username, hashed_password=user.hashed_password, email=user.email, avatar=user.avatar, description=user.description)
        last_record_id = await database.execute(query)
        return last_record_id
    except pymysql.err.IntegrityError as e:
        return None
    except Exception as e:
        print(e)
        return None


async def get_user(user_id: int, username: str) -> User:
    query = models.users.select()
    if user_id != 0:
        query = query.where(models.users.c.id == user_id)
    elif username != "":
        query = query.where(models.users.c.username == username)
    else:
        return None
    return await database.fetch_one(query)

import time

from fastapi import Depends, Request, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import ORJSONResponse
import jwt

from kaiyuanshe_werobot.settings import settings
from kaiyuanshe_werobot.db.database import database
from kaiyuanshe_werobot import const


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["auth"] = str(process_time)
    return response


async def auth(request, call_next):
    url = request.url.path
    if url in const.WHITE_LIST:
        return await call_next(request)
    token = request.headers.get('token')
    if not token:
        return ORJSONResponse(status_code=403, content="Forbidden")
    try:

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            return ORJSONResponse(status_code=400, content="invalid token")
    except jwt.exceptions.PyJWTError:
        return ORJSONResponse(status_code=400, content="invalid token")
    return await call_next(request)


async def start_up():
    await database.connect()


async def shutdown():
    await database.disconnect()

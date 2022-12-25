import hashlib

import werobot
from fastapi import FastAPI, Request

from kaiyuanshe_werobot.settings import settings
from kaiyuanshe_werobot.routers import auth, users

# todo: encoding_aes_key should be set in env
robot = werobot.WeRoBot(token=settings.WX_TOKEN, app_id=settings.APP_ID)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)

app.middleware()


@robot.handler
def hello(message):
    return settings.default_reply


@app.get("/")
async def home(signature, echostr, timestamp, nonce):
    expected_signature = hashlib.sha1("".join(sorted([settings.token, timestamp, nonce])).encode("utf-8")).hexdigest()
    if signature == expected_signature:
        return int(echostr)


@app.post("/")
async def home(request: Request, signature, timestamp):
    message = robot.parse_message(
        await request.body(),
        timestamp=timestamp,
        nonce=timestamp,
        msg_signature=signature
    )
    return robot.get_encrypted_reply(message)

import hashlib

import werobot
from fastapi import FastAPI, Request

from .settings import settings

# todo: encoding_aes_key should be set in env
robot = werobot.WeRoBot(token=settings.token, app_id=settings.app_id)

app = FastAPI()


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

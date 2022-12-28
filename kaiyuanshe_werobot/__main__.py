import hashlib

import werobot
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from kaiyuanshe_werobot.settings import settings
from kaiyuanshe_werobot.api import api
from kaiyuanshe_werobot.middleware import start_up, shutdown, auth

# todo: encoding_aes_key should be set in env
robot = werobot.WeRoBot(token=settings.WX_TOKEN, app_id=settings.APP_ID)

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


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        default_response_class=ORJSONResponse
    )
    application.include_router(api.api_router)
    application.add_event_handler("startup", start_up)
    application.add_event_handler("shutdown", shutdown)
    application.middleware("http")(auth)
    return application


app = get_application()

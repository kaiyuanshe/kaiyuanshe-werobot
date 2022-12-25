from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DEBUG: bool = True
    WX_TOKEN: str = "weixin"
    DEFAULT_REPLY: str = "欢迎关注开源社公众号，目前还在开发中，敬请期待！"
    ENCODING_AES_KEY: str = "sss"
    APP_ID: str = "sss"

    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = AppSettings()

if settings.DEBUG:
    print('=' * 20)
    for k, v in settings.dict().items():
        print(f'[system-config Config] {k} = {v}')
    print('=' * 20, flush=True)

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = True
    token: str = "weixin"
    default_reply: str = "欢迎关注开源社公众号，目前还在开发中，敬请期待！"


settings = AppSettings()

if settings.debug:
    print('=' * 20)
    for k, v in settings.dict().items():
        print(f'[system-config Config] {k} = {v}')
    print('=' * 20, flush=True)

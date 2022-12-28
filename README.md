kaiyuanshe-werobot
====

## What is WeRoBot?
A robot for kaiyuanshe's public account of wechat, aim to make it easy to reply user's message.  

## migrate db
```shell
# DATABASE_URL is the url of database,set in env before migrate
aerich init -t init_db.TORTOISE_ORM
aerich init-db
aerich migrate
aerich upgrade

# reverse
aerich downgrade
```

import os

class DB:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    name = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

class TG:
    token = os.getenv("TG_TOKEN")

class Config:
    db = DB()
    tg = TG()
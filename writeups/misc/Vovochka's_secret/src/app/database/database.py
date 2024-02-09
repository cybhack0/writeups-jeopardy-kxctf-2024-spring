import psycopg2 as psql
from models.command_status import *

class Database:
    def __init__(self, db_config):
        db_name = db_config.name
        db_host = db_config.host
        db_port = db_config.port
        db_user = db_config.user
        db_password = db_config.password
        
        self._db_con = psql.connect(host = db_host,
            port = db_port,
            database = db_name,
            user = db_user,
            password = db_password
        )
    
    def add_telegram_user(self, telegram_id):
        cursor = self._db_con.cursor()
        sqlRequest = """INSERT INTO users (telegram_id, status_code) VALUES (%s, %s)""" 
        cursor.execute(sqlRequest, (telegram_id, Status.NOTHING))
        self._db_con.commit()

    def is_user_exists(self, telegram_id):
        cursor = self._db_con.cursor()
        sqlRequest = """SELECT * FROM users WHERE telegram_id=%s""" 
        cursor.execute(sqlRequest, (telegram_id, ))

        return cursor.fetchone() is not None
    
    def update_status(self, telegram_id, status):
        cursor = self._db_con.cursor()
        sqlRequest = """UPDATE users SET status_code=%s WHERE telegram_id=%s""" 
        cursor.execute(sqlRequest, (status, telegram_id))
        self._db_con.commit()
    
    def get_user_status(self, telegram_id):
        cursor = self._db_con.cursor()
        sqlRequest = """SELECT status_code FROM users WHERE telegram_id=%s""" 
        cursor.execute(sqlRequest, (telegram_id, ))

        return cursor.fetchone()[0]
    
    def create_secret(self, name, timestamp, secret, password):
        cursor = self._db_con.cursor()
        sqlRequest = """INSERT INTO secrets (name, creation_time, secret, password) VALUES (%s, %s, %s, %s)""" 
        cursor.execute(sqlRequest, (name, timestamp, secret, password))

        self._db_con.commit()

    def is_secret_exists(self, name, password):
        cursor = self._db_con.cursor()
        sqlRequest = """SELECT * FROM secrets WHERE name=%s AND password=%s""" 
        cursor.execute(sqlRequest, (name, password))

        return cursor.fetchone() is not None
    
    def get_secret(self, name, password):
        cursor = self._db_con.cursor()
        sqlRequest = """SELECT secret FROM secrets WHERE name=%s AND password=%s""" 
        cursor.execute(sqlRequest, (name, password))

        return cursor.fetchone()[0]
    
    def get_secrets(self):
        cursor = self._db_con.cursor()
        sqlRequest = """SELECT name, creation_time FROM secrets""" 
        cursor.execute(sqlRequest)

        return cursor.fetchall()
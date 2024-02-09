import psycopg2 as psql
import time 
import os

SLEEPER = 60 * 1

class Database:
    def __init__(self):
        db_name = os.getenv("DB_NAME")
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DP_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        
        self._db_con = psql.connect(host = db_host,
            port = db_port,
            database = db_name,
            user = db_user,
            password = db_password
        )

    def delete(self):
        cursor = self._db_con.cursor()
        sqlRequest = """DELETE FROM secrets WHERE id <> 1""" 
        cursor.execute(sqlRequest)
        self._db_con.commit()


db = Database()

while True:
    db.delete()
    time.sleep(SLEEPER)
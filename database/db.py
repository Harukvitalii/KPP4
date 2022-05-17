
import psycopg2
from config import HOST, db_name, password, user,port
import json
from psycopg2.errors import UniqueViolation
        
class PGBOTDB:
    def __init__(self):
        self.conn = psycopg2.connect(
        host=HOST,
        user = user,
        password = password,
        database=db_name,
        port = port,
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    """USERS TABLE"""
    def create_tables(self):
        """SET TIME ZONE"""
        self.cursor.execute("""SET TIME ZONE 'Europe/Moscow';""")
        
        """users"""
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                id serial NOT NULL PRIMARY KEY,
                first_name varchar(50),
                nick_name varchar(50),
                user_id bigint UNIQUE NOT NULL,
                );""")
        self.conn.commit()

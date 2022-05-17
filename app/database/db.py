
import psycopg2
from app.config import HOST, db_name, password, user,port
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
            """CREATE TABLE IF NOT EXISTS kpp4(
                id serial NOT NULL PRIMARY KEY,
                chat_id int NOT NULL,
                name varchar(50),
                text varchar(750)
                );""")
        self.conn.commit()


    def add_text(self, name,text,chat_id=1):
        """Добавляєм запись в чат"""
        if 'GET /' in name or 'GET /' in text:
            return 0
        if 'GET /favicon.ico' in name or 'GET /favicon.ico' in text: 
            return 0

        self.cursor.execute("""INSERT INTO kpp4 
        (chat_id,name, text) VALUES 
        (%s,%s,%s);""",
        (chat_id, name, text))


    def get_chat_data(self,chat_id):
        'Забераєм всі данні'
        self.cursor.execute("""SELECT * FROM kpp4 WHERE chat_id = %s;
        """,(chat_id,))
        res = self.cursor.fetchall()
        return res


     
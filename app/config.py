from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.getenv('HOST')
user = os.getenv('user')
password = os.getenv('password')
db_name = os.getenv('db_name')
port = os.getenv('port')
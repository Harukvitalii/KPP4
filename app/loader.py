from app.database.db import PGBOTDB


pgbotdb = PGBOTDB()
pgbotdb.create_tables()
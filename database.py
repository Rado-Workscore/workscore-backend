from databases import Database
import sqlalchemy

DATABASE_URL = "postgresql://barssrado@localhost/workscore_db"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


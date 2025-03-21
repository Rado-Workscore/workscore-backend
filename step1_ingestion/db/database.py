from databases import Database
import sqlalchemy

DATABASE_URL = "postgresql://workscore_db_user:himcx6zc5rcHirVIKfmSSTh0eI5CgBmM@dpg-cvctgdtrie7s739jhvn0-a.oregon-postgres.render.com/workscore_db"

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


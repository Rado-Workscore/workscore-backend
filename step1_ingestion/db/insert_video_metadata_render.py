import os
import sqlalchemy
from datetime import datetime
from database import database
from models import metadata

# Տվյալ ֆայլի ուղին
video_path = "step1_ingestion/videos/warehouse_1_compressed.mp4"

# Ստուգում ենք՝ արդյոք ֆայլը գոյություն ունի
if not os.path.exists(video_path):
    print(f"❌ Ֆայլը չի գտնվել՝ {video_path}")
    exit()

# Ստանում ենք ֆայլի չափը (MB)
file_size = round(os.path.getsize(video_path) / (1024 * 1024), 2)

# Գրանցվող տվյալները
record = {
    "warehouse_id": 1,
    "filename": os.path.basename(video_path),
    "filesize_mb": file_size
}

# Սահմանում ենք աղյուսակը՝ SQLAlchemy Table
video_metadata = sqlalchemy.Table(
    "video_metadata",
    metadata,
    autoload_with=sqlalchemy.create_engine(str(database.url))
)

# Կապ ենք հաստատում engine-ի հետ
engine = sqlalchemy.create_engine(str(database.url))
with engine.connect() as conn:
    conn.execute(video_metadata.insert().values(**record))
    conn.commit()

print("✅ Մետատվյալները հաջողությամբ գրանցվեցին PostgreSQL բազայում Render-ում։")

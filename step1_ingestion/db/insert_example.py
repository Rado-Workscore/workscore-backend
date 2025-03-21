import sqlalchemy
from database import database
from models import employees

example = {
    "employee_id": "E001",
    "accuracy_score": 95.0,
    "compliance_score": 90.0,
    "speed_score": 85.0,
    "trajectory_score": 88.0,
    "work_score": 89.5
}

engine = sqlalchemy.create_engine(str(database.url))

with engine.connect() as conn:
    conn.execute(employees.insert().values(**example))
    conn.commit()

print("✅ Օրինակային տվյալն ավելացվեց։")


from sqlalchemy import Table, Column, Integer, String, Float
from database import metadata

employees = Table(
    "employees",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("employee_id", String, unique=True, index=True),
    Column("accuracy_score", Float),
    Column("compliance_score", Float),
    Column("speed_score", Float),
    Column("trajectory_score", Float),
    Column("work_score", Float)
)


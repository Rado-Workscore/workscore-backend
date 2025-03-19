from sqlalchemy import Table, Column, Integer, String, Float, MetaData
from sqlalchemy.orm import declarative_base

Base = declarative_base()  # Սրանք թույլ կտան Alembic-ին հայտնաբերել մոդելները
metadata = Base.metadata  

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)
    accuracy_score = Column(Float)
    compliance_score = Column(Float)
    speed_score = Column(Float)
    trajectory_score = Column(Float)
    work_score = Column(Float)



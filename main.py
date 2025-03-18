from fastapi import FastAPI, File, UploadFile
import shutil
import os

app = FastAPI()

# Ստեղծում ենք վիդեոների պահպանման պանակ
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "WorkScore Backend is Running!"}
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from security import create_access_token, get_current_user

app = FastAPI()

class User(BaseModel):
    username: str

# Ստեղծել token (login)
@app.post("/token")
async def login(user: User):
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Ստուգել token (authenticated route)
@app.get("/users/me")
async def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "Video uploaded successfully"}
import cv2

@app.get("/video-info/")
def get_video_info(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    cap = cv2.VideoCapture(file_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    return {"filename": filename, "total_frames": frame_count}
from fastapi import FastAPI
from database import database
from models import employees

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/employees", summary="Ստանալ բոլոր աշխատակիցների տվյալները")
async def get_employees():
    query = employees.select()
    return await database.fetch_all(query)
from pydantic import BaseModel

# Մոդել տվյալների համար (նոր աշխատակցի տվյալներ)
class EmployeeCreate(BaseModel):
    employee_id: str
    accuracy_score: float
    compliance_score: float
    speed_score: float
    trajectory_score: float
    work_score: float

@app.post("/employees", summary="Ավելացնել նոր աշխատակից")
async def create_employee(employee: EmployeeCreate):
    query = employees.insert().values(
        employee_id=employee.employee_id,
        accuracy_score=employee.accuracy_score,
        compliance_score=employee.compliance_score,
        speed_score=employee.speed_score,
        trajectory_score=employee.trajectory_score,
        work_score=employee.work_score
    )
    await database.execute(query)
    return {"message": "✅ Աշխատակիցը հաջողությամբ ավելացվեց!"}






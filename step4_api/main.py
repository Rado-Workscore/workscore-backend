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

@app.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "Video uploaded successfully"}
@app.get("/health")
def health_check():
    return {"status": "API is live!"}








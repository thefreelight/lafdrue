from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        # 处理文件覆盖
        if os.path.exists(file_location):
            os.remove(file_location)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload image: {e}")

    return JSONResponse(content={"url": f"/{file_location}"})

@router.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    try:
        # 处理文件覆盖
        if os.path.exists(file_location):
            os.remove(file_location)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to upload video: {e}")

    return JSONResponse(content={"url": f"/{file_location}"})

from fastapi import APIRouter, UploadFile, File, Form
import shutil
import uuid
import os

from app.services.detector import predict_image

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/webcam/predict")
async def webcam_predict(
    file: UploadFile = File(...),
    confidence: float = Form(0.10)
):
    filename = f"{uuid.uuid4()}.jpg"
    image_path = os.path.join(UPLOAD_DIR, filename)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Return exactly what predict_image() returns
    return predict_image(image_path, confidence)
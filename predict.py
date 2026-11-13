from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.detector import predict_image

router = APIRouter()


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    image_path = f"uploads/{file.filename}"

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    result = predict_image(image_path)

    return result
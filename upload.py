from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
import zipfile

router = APIRouter()

os.makedirs("uploads", exist_ok=True)
os.makedirs("datasets", exist_ok=True)


@router.post("/upload-dataset")
async def upload_dataset(file: UploadFile = File(...)):

    if not file.filename.endswith(".zip"):
        raise HTTPException(
            status_code=400,
            detail="Only ZIP datasets are allowed."
        )

    zip_path = f"uploads/{file.filename}"

    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    dataset_name = file.filename.replace(".zip", "")
    extract_path = f"datasets/{dataset_name}"

    os.makedirs(extract_path, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return {
        "message": "Dataset uploaded and extracted successfully.",
        "dataset": dataset_name,
        "location": extract_path
    }
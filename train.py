from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
import uuid

from app.services.trainer import train_yolo
from app.job_store import jobs

router = APIRouter()


class TrainRequest(BaseModel):
    dataset: str
    epochs: int = 5
    imgsz: int = 640


@router.post("/train")
def train_model(request: TrainRequest, background_tasks: BackgroundTasks):

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "Queued",
        "progress": 0
    }

    background_tasks.add_task(
        train_yolo,
        job_id,
        request.dataset,
        request.epochs,
        request.imgsz
    )

    return {
        "message": "Training started.",
        "job_id": job_id
    }
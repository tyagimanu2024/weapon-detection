from fastapi import APIRouter
from app.job_store import jobs

router = APIRouter()


@router.get("/status/{job_id}")
def training_status(job_id: str):

    if job_id not in jobs:
        return {
            "error": "Job not found."
        }

    return jobs[job_id]
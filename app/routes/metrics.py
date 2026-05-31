from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import SessionLocal
from app.models.inference_log import InferenceLog

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):

    total_requests = db.query(InferenceLog).count()

    avg_latency = db.query(
        func.avg(InferenceLog.latency)
    ).scalar()

    avg_confidence = db.query(
        func.avg(InferenceLog.confidence)
    ).scalar()

    return {
        "total_requests": db.query(InferenceLog).count(), #total_requests
        "average_latency": db.query(func.avg(InferenceLog.latency)).scalar() or 0, #round(avg_latency or 0, 3),
        "average_confidence": db.query(func.avg(InferenceLog.confidence)).scalar() or 0, #round(avg_confidence or 0, 3)
    }

@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    logs = db.query(InferenceLog).all()

    return [
        {
            "id": log.id,
            "prompt": log.prompt,
            "response": log.response,
            "latency": log.latency,
            "confidence": log.confidence,
            "status": log.status,
            "created_at": log.created_at
        }
        for log in logs
    ]
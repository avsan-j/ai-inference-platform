from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.inference_log import InferenceLog
from app.schemas.inference import (
    InferenceRequest,
    InferenceResponse
)
from app.services.inference_service import run_inference

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/infer", response_model=InferenceResponse)
def infer(
    request: InferenceRequest,
    db: Session = Depends(get_db)
):

    result = run_inference(request.prompt)

    log = InferenceLog(
        prompt=request.prompt,
        response=result["response"],
        confidence=result["confidence"],
        latency=result["latency"],
        status=result["status"]
    )

    db.add(log)
    db.commit()

    return result

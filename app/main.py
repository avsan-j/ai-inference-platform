from fastapi import FastAPI

from app.database import Base, engine
from app.routes.inference import router as inference_router
from app.routes.metrics import router as metrics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Inference Monitoring Platform"
)

app.include_router(inference_router)
app.include_router(metrics_router)
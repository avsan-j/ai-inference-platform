from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime, timezone

from app.database import Base

class InferenceLog(Base):

    __tablename__ = "inference_logs"

    id = Column(Integer, primary_key=True, index=True)

    prompt = Column(String, nullable=False)

    response = Column(String, nullable=False)

    confidence = Column(Float)

    latency = Column(Float)

    status = Column(String)

    created_at = Column(DateTime, default=datetime.now(timezone.utc))
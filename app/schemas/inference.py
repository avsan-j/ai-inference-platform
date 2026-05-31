from pydantic import BaseModel

class InferenceRequest(BaseModel):
    prompt: str

class InferenceResponse(BaseModel):
    response: str
    confidence: float
    latency: float
    status: str
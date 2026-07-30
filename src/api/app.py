
# app.py
# Placeholder API for serving model inference

from fastapi import FastAPI
from src.inference.baseline_inference import run_inference
from src.logging.logger import log_event

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    """
    Simple health check endpoint.
    Confirms the API is running.
    """
    return {"status": "ok"}

@app.post("/predict")
def predict():
    """
    Placeholder prediction endpoint.
    Will call the inference pipeline once implemented.
    """
    raise NotImplementedError("Prediction endpoint not implemented yet.")

# app.py
# Placeholder API for serving model inference

from fastapi import FastAPI
from src.inference.baseline_inference import run_inference
from src.logging.logger import log_event

# Retailer lookup table
RETAILER_LINKS = {
    "Santa Cruz Nomad": "https://www.backcountry.com/santa-cruz-nomad"
}

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

    # Temporary placeholder values
    predicted_class = "test_prediction"
    confidence = 0.99

    # Retailer lookup (only returns a URL for Nomad)
    retailer_url = RETAILER_LINKS.get(predicted_class)

    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "retailer_url": retailer_url
    }


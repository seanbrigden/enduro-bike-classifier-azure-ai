# app.py
# FastAPI endpoint serving real model inference

from fastapi import FastAPI, UploadFile, File
from src.inference.baseline_inference import run_inference
from src.logging.logger import log_event
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

# Retailer lookup table
RETAILER_LINKS = {
    "Santa Cruz Nomad": "https://www.backcountry.com/santa-cruz-nomad"
}

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Real prediction endpoint.
    Receives an uploaded image, runs inference, returns prediction + confidence.
    """

    # Read image bytes
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Run your real inference pipeline
    predicted_class, confidence = run_inference(image)

    # Retailer lookup (only returns a URL for Nomad)
    retailer_url = RETAILER_LINKS.get(predicted_class)

    # Log the event
    log_event(f"Prediction: {predicted_class}, Confidence: {confidence}")

    return {
        "prediction": predicted_class,
        "confidence": confidence,
        "retailer_url": retailer_url
    }

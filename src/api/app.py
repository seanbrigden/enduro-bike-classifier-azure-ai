# app.py
# FastAPI service: serves the UI and runs local ONNX inference.

from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from src.inference.baseline_inference import get_classifier, run_inference
from src.logging.logger import log_event

REPO_ROOT = Path(__file__).resolve().parents[2]
UI_FILE = REPO_ROOT / "src" / "ui" / "index.html"

MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB

# Keyed by the raw label in labels.txt, not the display name.
RETAILER_LINKS = {
    "santa_cruz_nomad": "https://www.backcountry.com/search?s=u&q=santa+cruz+nomad",
}

app = FastAPI(title="Enduro Bike Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # local dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def warm_model():
    """Load the ONNX session at startup so the first demo click isn't slow."""
    get_classifier()
    log_event("Model loaded and ready")


@app.get("/")
def serve_ui():
    """Serve the UI from the same origin as the API."""
    return FileResponse(UI_FILE)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not (file.content_type or "").startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    contents = await file.read()
    if not contents:
        raise HTTPException(status_code=400, detail="Uploaded file was empty.")
    if len(contents) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="Image is larger than 10 MB.")

    try:
        result = run_inference(contents)
    except Exception as exc:
        log_event(f"Inference failed: {exc}")
        raise HTTPException(status_code=500, detail="Could not process that image.")

    label = result["label"]
    confident = result["is_confident"]

    log_event(
        f"Prediction: {label} ({result['confidence']:.3f}) "
        f"confident={confident} file={file.filename}"
    )

    # Below the threshold we don't name a bike and we don't show a buy link.
    if not confident:
        return {
            "prediction": "Not confident enough to call it",
            "confidence": result["confidence"],
            "retailer_url": None,
            "probabilities": result["probabilities"],
            "note": "This model only knows two frames. Closest match was "
                    f"{result['display_name']}.",
        }

    return {
        "prediction": result["display_name"],
        "confidence": result["confidence"],
        "retailer_url": RETAILER_LINKS.get(label),
        "probabilities": result["probabilities"],
    }

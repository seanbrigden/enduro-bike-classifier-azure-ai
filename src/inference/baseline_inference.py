# baseline_inference.py
# Baseline inference pipeline for local MVP testing

import io
from PIL import Image

def run_inference(image_bytes: bytes):
    """
    Baseline inference function.
    For MVP: loads the image, performs a simple check, and returns a fake prediction.
    Later: replace this with Azure Custom Vision inference.
    """

    # Load image from bytes
    try:
        image = Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        raise ValueError(f"Could not load image: {e}")

    # ---------------------------------------------------------
    # MVP LOGIC (temporary)
    # ---------------------------------------------------------
    # This is where your real model will go.
    # For now, we return a deterministic placeholder so your API works end-to-end.

    # Example: simple heuristic based on image size (just for demo)
    width, height = image.size

    if width > height:
        predicted_class = "Santa Cruz Nomad"
        confidence = 0.88
    else:
        predicted_class = "Specialized Enduro"
        confidence = 0.91

    return predicted_class, confidence

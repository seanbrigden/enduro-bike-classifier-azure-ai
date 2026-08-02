# baseline_inference.py
# Local ONNX inference for the Custom Vision compact export.

import io
import json
import os
from pathlib import Path

import numpy as np
import onnxruntime as ort
from PIL import Image

# Absolute paths, so this works no matter which directory you run from.
REPO_ROOT = Path(__file__).resolve().parents[2]
MODEL_DIR = REPO_ROOT / "src" / "model" / "enduro_classifier"
MODEL_PATH = MODEL_DIR / "model.onnx"
LABELS_PATH = MODEL_DIR / "labels.txt"
METADATA_PATH = MODEL_DIR / "metadata_properties.json"

# Raw label (from labels.txt) -> name shown to a human.
DISPLAY_NAMES = {
    "santa_cruz_nomad": "Santa Cruz Nomad V6",
    "specialized_enduro": "Specialized Enduro",
    "other": "Not a Nomad or an Enduro",
}

# Below this, we return "not confident" even if a class wins outright.
CONFIDENCE_THRESHOLD = 0.70


class EnduroClassifier:
    def __init__(self):
        with open(LABELS_PATH) as f:
            self.labels = [line.strip() for line in f if line.strip()]

        self.session = ort.InferenceSession(
            str(MODEL_PATH), providers=["CPUExecutionProvider"]
        )

        model_input = self.session.get_inputs()[0]
        self.input_name = model_input.name

        # Read the target size off the model itself rather than hard-coding it.
        # This export is [1, 3, 300, 300]; reading it means a re-export at a
        # different resolution won't silently break inference.
        _, _, height, width = model_input.shape
        self.target_size = (int(width), int(height))

        if METADATA_PATH.exists():
            with open(METADATA_PATH) as f:
                self.metadata = json.load(f)
        else:
            self.metadata = {}

    @staticmethod
    def _to_pil(image):
        """Accept raw bytes, a file-like object, a path, or a PIL Image."""
        if isinstance(image, Image.Image):
            return image.convert("RGB")
        if isinstance(image, (bytes, bytearray)):
            return Image.open(io.BytesIO(image)).convert("RGB")
        if hasattr(image, "read"):
            return Image.open(image).convert("RGB")
        if isinstance(image, (str, os.PathLike, Path)):
            return Image.open(image).convert("RGB")
        raise TypeError(f"Unsupported image input: {type(image)!r}")

    def preprocess(self, image):
        img = self._to_pil(image)

        # metadata_properties.json specifies ResizeMethod=Stretch, so a plain
        # resize to the model's target size is correct here.
        img = img.resize(self.target_size)

        arr = np.array(img).astype(np.float32) / 255.0  # NominalPixelRange: 0-1
        arr = np.transpose(arr, (2, 0, 1))  # HWC -> CHW
        return np.expand_dims(arr, axis=0)  # add batch dim

    def predict(self, image):
        tensor = self.preprocess(image)
        raw = self.session.run(None, {self.input_name: tensor})[0][0]

        # This export already applies softmax inside the graph, so its output
        # sums to 1. Applying softmax a second time would flatten a 99%
        # prediction down to ~73%. Only normalize if the output is not
        # already a probability distribution.
        if abs(float(raw.sum()) - 1.0) > 1e-3:
            shifted = np.exp(raw - np.max(raw))
            probs = shifted / shifted.sum()
        else:
            probs = raw

        idx = int(np.argmax(probs))
        label = self.labels[idx]
        confidence = float(probs[idx])

        return {
            "label": label,
            "display_name": DISPLAY_NAMES.get(label, label),
            "confidence": confidence,
            "is_confident": confidence >= CONFIDENCE_THRESHOLD,
            "probabilities": {
                self.labels[i]: float(probs[i]) for i in range(len(self.labels))
            },
        }


# Load the model once per process, not once per request. Creating an
# InferenceSession reads 44MB off disk and takes seconds.
_classifier = None


def get_classifier() -> EnduroClassifier:
    global _classifier
    if _classifier is None:
        _classifier = EnduroClassifier()
    return _classifier


def run_inference(image):
    """Returns a dict. Accepts bytes, a file-like object, or a path."""
    return get_classifier().predict(image)

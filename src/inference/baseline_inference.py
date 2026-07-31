# baseline_inference.py
# Baseline inference pipeline for local MVP testing

import onnxruntime as ort
import numpy as np
from PIL import Image
import os

# Paths relative to repo root
MODEL_PATH = os.path.join("src", "model", "enduro_classifier", "model.onnx")
LABELS_PATH = os.path.join("src", "model", "enduro_classifier", "labels.txt")


class EnduroClassifier:
    def __init__(self):
        # Load labels
        with open(LABELS_PATH, "r") as f:
            self.labels = [line.strip() for line in f.readlines()]

        # Load ONNX model
        self.session = ort.InferenceSession(
            MODEL_PATH,
            providers=["CPUExecutionProvider"]
        )

        # Get model input name
        self.input_name = self.session.get_inputs()[0].name

    def preprocess(self, image_path):
        img = Image.open(image_path).convert("RGB")

        # Azure Custom Vision ONNX models expect 224x224
        img = img.resize((224, 224))

        img = np.array(img).astype(np.float32)

        # Normalize to 0–1
        img = img / 255.0

        # Convert HWC → CHW
        img = np.transpose(img, (2, 0, 1))

        # Add batch dimension
        img = np.expand_dims(img, axis=0)

        return img

    def predict(self, image_path):
        img = self.preprocess(image_path)

        outputs = self.session.run(None, {self.input_name: img})
        logits = outputs[0][0]

        # Softmax
        exp = np.exp(logits - np.max(logits))
        probs = exp / exp.sum()

        # Highest probability class
        idx = np.argmax(probs)
        label = self.labels[idx]
        confidence = float(probs[idx])

        return {
            "label": label,
            "confidence": confidence,
            "probabilities": {
                self.labels[i]: float(probs[i])
                for i in range(len(self.labels))
            }
        }


def run_inference(image_path):
    classifier = EnduroClassifier()
    return classifier.predict(image_path)

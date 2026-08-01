# test_inference.py
# Quick local test runner for the ONNX inference pipeline.
# Run from the repo root:  python -m src.inference.test_inference <image_path>

import sys
from pathlib import Path

from src.inference.baseline_inference import run_inference


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.inference.test_inference <image_path>")
        return

    image_path = Path(sys.argv[1])
    if not image_path.exists():
        print(f"Error: File not found -> {image_path}")
        return

    result = run_inference(image_path)

    print("\n=== Inference Result ===")
    print(f"Predicted: {result['display_name']}")
    print(f"Confidence: {result['confidence']:.4f}")
    print(f"Above threshold: {result['is_confident']}")
    print("\nFull probabilities:")
    for label, prob in result["probabilities"].items():
        print(f"  {label}: {prob:.4f}")


if __name__ == "__main__":
    main()

# test_inference.py
# Quick local test runner for the ONNX inference pipeline

from baseline_inference import run_inference
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_inference.py <image_path>")
        return

    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print(f"Error: File not found -> {image_path}")
        return

    result = run_inference(image_path)
    print("\n=== Inference Result ===")
    print(f"Predicted Label: {result['label']}")
    print(f"Confidence: {result['confidence']:.4f}")
    print("\nFull Probabilities:")
    for label, prob in result["probabilities"].items():
        print(f"  {label}: {prob:.4f}")

if __name__ == "__main__":
    main()

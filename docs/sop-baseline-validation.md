# SOP: Baseline Azure Vision Validation

## Purpose
Evaluate whether Azure Vision can reliably detect and classify the chosen bike silhouettes using the golden image set.

---

## Steps

### 1. Upload Golden Images
Upload all images from `/data/golden/<model>/` into Azure Vision (Custom Vision or Vision Studio).

### 2. Run Baseline Classification
For each image:
- Run object detection or classification
- Record confidence scores
- Note misclassifications

### 3. Evaluate Performance
Check for:
- Consistent detection across colourways
- Misclassifications between similar silhouettes
- Any generation-related confusion
- Any colour-related bias

### 4. Document Findings
Record:
- Accuracy trends
- Failure cases
- Observed patterns
- Recommendations for dataset adjustments

### 5. Adjust Dataset Spec (If Needed)
If issues arise:
- Add more colour variation
- Remove problematic images
- Tighten generation rules
- Add more clean profile shots

### 6. Approve Dataset for Full Collection
Dataset is approved when:
- Baseline detection is consistent
- No major silhouette confusion remains
- Colour bias is not observed

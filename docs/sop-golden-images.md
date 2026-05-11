# SOP: Golden Image Collection

## Purpose
Collect 10–20 perfect, representative images per class to validate the baseline Azure Vision model.

---

## Steps

### 1. Confirm Model Generation
Verify the correct generation for the model being collected.

### 2. Source Images
Use reputable sources:
- Pinkbike
- VitalMTB
- Manufacturer product pages
- Review sites
- High-quality user photos (if clean)

### 3. Apply Image Quality Criteria
Only accept images that meet:
- Full side profile
- Drive-side visible
- Clean background
- No rider
- Pedals installed (preferred)
- High resolution
- Correct generation

### 4. Ensure Colour Diversity
Before finalizing:
- Include 3–4 colourways per model
- Avoid colour-dominated sets

### 5. Save Images
Save to:

/data/golden/<model>/

Code

Use naming convention:

<model><source><index>.jpg

Code

### 6. Review and Approve
Remove any images that:
- Violate silhouette rules
- Include wrong generation
- Are low quality
- Introduce colour bias

---

## Completion Criteria
Golden set is complete when:
- 10–20 images per class are collected
- All images meet quality and generation rules
- Colour diversity is confirmed

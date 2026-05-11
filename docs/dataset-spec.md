# Enduro Bike Classifier — Dataset Specification (MVP)

## 1. Purpose
Define a clean, consistent dataset for training a 5‑class enduro bike classifier using Azure Vision Custom Models. This specification ensures consistent geometry, silhouette clarity, and high-quality training data.

---

## 2. Classes (One Generation Per Model)
To avoid geometry drift and ensure consistent silhouettes, each class represents a single generation:

- **Specialized Enduro — Gen 4 (2020+)**
- **Santa Cruz Nomad — V6 (2023+)**
- **Trek Slash — Gen 6 (2021+)**
- **Giant Reign — 2020+**
- **YT Capra — 2021+**

---

## 3. Image Requirements
Images must meet the following criteria:

### Required
- Full side profile
- Drive-side preferred
- Clean background (outdoor or studio)
- No rider blocking the frame
- No extreme angles (avoid fisheye, GoPro distortion)
- High resolution
- Pedals installed (preferred)

### Strongly Preferred
- Clear visibility of suspension linkage
- No heavy shadows or glare
- No mud or debris obscuring silhouette

---

## 4. Exclusions
Do **not** include:

- Older generations with different geometry
- Bikes with racks, bags, child seats, or accessories
- Artistic edits, filters, or colour distortions
- Cropped frames or partial bikes
- Images with riders blocking linkage
- Extreme angles or motion blur

---

## 5. Colour Variation Requirements
To prevent colour-based bias:

- Include **multiple colourways** per model
- Avoid datasets where one model is dominated by a single colour
- Golden images must include **3–4 distinct colour variations**
- Colour must not be used as a classification signal

---

## 6. Dataset Size (MVP)
- **Golden set:** 10–20 perfect images per class  
- **Training set (Phase 1):** 50–100 images per class  
- **Validation/Test:** 20–30% split from processed dataset

---

## 7. Folder Structure


# Image Guidelines — Enduro Bike Classifier

These guidelines ensure consistent, high-quality images for both the golden set and the full dataset.

---

## 1. Good Image Examples
Images should have:

- Full side profile
- Drive-side visible
- Clean, uncluttered background
- Pedals installed
- Clear visibility of suspension linkage
- High resolution
- Natural lighting
- No rider present

---

## 2. Bad Image Examples
Avoid images with:

- Rider blocking the frame
- Cropped wheels or missing frame sections
- Mud, dirt, or debris obscuring silhouette
- Extreme angles (front-on, rear-on, fisheye)
- Heavy shadows or glare
- Indoor clutter (garage chaos, storage rooms)
- Filters, edits, or colour distortions
- No pedals *and* crank rotated vertically (misleading silhouette)

---

## 3. Colour Variation Requirements
To prevent colour-based overfitting:

- Include multiple colourways per model
- Avoid datasets dominated by a single colour
- Ensure golden images include at least 3–4 colour variations

---

## 4. Generation Consistency
Each model must use **one generation only**:

- Specialized Enduro (2020+)
- Santa Cruz Nomad (V6)
- Trek Slash (Gen 6)
- Giant Reign (2020+)
- YT Capra (2021+)

Do not mix older generations with different geometry.

---

## 5. File Naming Convention
Use consistent naming:
<model><source><index>.jpg
Example:
trek_slash_pinkbike_01.jpg

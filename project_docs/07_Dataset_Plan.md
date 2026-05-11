# Dataset Plan

## 1. Purpose
Define the data required to train, validate, and test a baseline mountain bike classifier using Azure Vision. This plan outlines sources, structure, labeling, quality standards, and risks. It supports the MVP and provides a foundation for future custom model training.

---

## 2. Dataset Scope

### 2.1 MVP Scope
The MVP will classify **bike brand only** (e.g., Specialized, Trek, Giant, Santa Cruz).

- Target classes: 4–6 major brands
- Image types: side-profile photos of enduro-style mountain bikes
- Minimum images per class: 50–100
- Total dataset size: ~300–600 images

### 2.2 Future Scope (Not in MVP)
- Model-level classification (e.g., Specialized Enduro vs. Stumpjumper)
- Year/model variant classification
- Additional categories (trail, XC, downhill)
- Real-world trail photos with occlusion, mud, riders, etc.

---

## 3. Data Sources

### 3.1 Primary Sources (MVP)
- Manufacturer websites (public product photos)
- Bike review sites (e.g., Pinkbike, VitalMTB)
- Retailer listings (e.g., JensonUSA, Chain Reaction Cycles)
- User-uploaded images from forums (only if allowed)

### 3.2 Secondary Sources (Future)
- Scraped images with automated filtering
- User-submitted images (if building a UI later)
- Bike park cameras (hypothetical commercial extension)

---

## 4. Data Collection Approach

### 4.1 Manual Collection (MVP)
- Manually download 50–100 images per brand
- Ensure variety in:
  - angles (but mostly side-profile)
  - lighting
  - backgrounds
  - colorways
  - wheel sizes

### 4.2 Automated Collection (Future)
- Web scraping with filtering
- Automated deduplication
- Automated EXIF stripping

---

## 5. Dataset Structure

### 5.1 Folder Layout (MVP)
/dataset
/raw
/specialized
/trek
/giant
/santacruz
/processed
/train
/val
/test

### 5.2 Train/Val/Test Split
- Train: 70%
- Validation: 15%
- Test: 15%

---

## 6. Labeling Strategy

### 6.1 MVP Labeling
- Folder-based labeling (Azure Vision supports this)
- Each folder = one brand
- No bounding boxes or segmentation required

### 6.2 Future Labeling
- Model-level labels
- Frame material
- Suspension type
- Geometry metadata (if available)

---

## 7. Quality Standards

### 7.1 Image Requirements
- Minimum resolution: 600px on shortest side
- No watermarks if possible
- No riders in frame (MVP)
- Bike must be at least 60% of the image

### 7.2 Dataset Quality Checks
- Remove duplicates
- Remove blurry images
- Ensure class balance (±20%)

---

## 8. Risks & Mitigations

### **Risk 1: Class imbalance**
- *Mitigation:* Oversample minority classes or collect more images.

### **Risk 2: Low-quality or inconsistent images**
- *Mitigation:* Manual review; enforce quality standards.

### **Risk 3: Copyright concerns**
- *Mitigation:* Use publicly available product images; avoid scraping protected content.

### **Risk 4: Overfitting to studio photos**
- *Mitigation:* Add real-world images in future iterations.

---

## 9. Acceptance Criteria (MVP)

- Dataset contains at least 50 images per brand
- All images meet quality standards
- Train/val/test split completed
- Folder structure matches architecture outline
- Dataset is ready for Azure Vision ingestion

---

## 10. Next Steps

- Begin manual image collection
- Create dataset folder structure in repo (or local)
- Prepare for Azure Vision baseline model training

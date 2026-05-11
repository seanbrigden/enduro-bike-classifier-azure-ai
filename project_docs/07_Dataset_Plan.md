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

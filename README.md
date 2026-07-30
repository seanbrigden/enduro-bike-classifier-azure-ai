Enduro + Nomad Bike Classifier (Azure AI)
A fully documented AI portfolio project that detects the brand and model of enduro mountain bikes using Azure AI services.
This project showcases end‑to‑end product thinking: data sourcing, model development, evaluation, deployment planning, and product management artifacts.

1. Problem
Bike marketplaces and customer service teams struggle with miscategorized or misrepresented listings.
This creates friction for:

Buyers – inaccurate search results and reduced trust

Sellers – incorrect categorization and lower visibility

Customer Service – manual verification of listings

Fraud Teams – difficulty identifying counterfeit or mislabeled products

A lightweight image classifier can automate brand/model detection and improve trust, search relevance, and operational efficiency.

2. Solution Overview
This MVP uses Azure Custom Vision to classify two high‑end enduro frames:

Santa Cruz Nomad V6

Specialized Enduro

The system includes:

a trained Custom Vision model

a Python inference pipeline

a demo notebook with example predictions

evaluation metrics

a roadmap for scaling to full marketplace coverage

3. Architecture Overview
Training:

Azure Custom Vision (image classification)

curated dataset of Nomad V6 + Enduro images

iterative training + evaluation

Inference:

Python script (src/inference.py)

REST API call to Custom Vision endpoint

returns top prediction + confidence score

Demo:

Jupyter notebook (notebooks/demo.ipynb)

runs predictions on sample images

includes commentary on model behavior

4. Current Capabilities
Detects Nomad V6 vs Enduro with strong precision

Handles multiple angles and backgrounds

Provides confidence scores for downstream decisioning

Supports batch or single‑image inference

5. Model Performance (Iteration 3)
Precision: XX%
Recall: XX%
Average Precision: XX%

Per‑Class Breakdown:

Nomad V6: recall gap due to geometry similarity

Enduro: strong recall, consistent silhouette detection

(Replace XX with your actual metrics.)

6. Demo Outputs
See notebooks/demo.ipynb for:

3–5 example predictions

confidence scores

commentary on correct vs borderline cases

7. Known Challenges
Nomad geometry is visually similar to other VPP frames

Background clutter affects recall

Dataset imbalance (Nomad < Enduro)

Limited generational coverage (V6 only)

8. Roadmap
This roadmap reflects the project’s evolution from concept → MVP → scalable product.

Completed
☑ Project Charter

☑ Scope Statement

☑ Requirements

☑ Risk Register

☑ Decision Log

☑ Architecture Outline

In Progress
☐ Dataset Plan

☐ Baseline Model (Azure Vision)

☐ Inference API

☐ Minimal UI Prototype

☐ Logging & Monitoring

☐ README Formatting & Presentation Cleanup (spacing, hierarchy, diagrams)

Future
☐ Custom Model Training (multi‑brand, multi‑model)

☐ Marketplace integration

☐ Fraud‑detection heuristics

☐ Feedback loop for continuous improvement

9. Status
This is an early‑stage MVP.
A cleaned‑up version will be published next week.

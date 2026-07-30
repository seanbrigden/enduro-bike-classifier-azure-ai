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

## 7. Folder Structure

The repository is organized into clear, modular components to support maintainability and future expansion.
project_root/
├── src/
│   ├── api/
│   │   └── app.py                 # FastAPI scaffold
│   ├── inference/
│   │   └── baseline_inference.py  # Baseline inference scaffold
│   ├── logging/
│   │   └── logger.py              # Logging scaffold
│   └── ui/
│       └── index.html             # Minimal UI scaffold
│
├── project_docs/
│   ├── 01_Project_Charter.md
│   ├── 02_Scope_Statement.md
│   ├── 03_Requirements.md
│   ├── 04_Risk_Register.md
│   ├── 05_Decision_Log.md
│   ├── 06_Architecture_Outline.md
│   ├── 07_Dataset_Plan.md
│   └── 08_Roadmap.md              # Full development roadmap
│
├── README.md
└── .gitignore


## 9. Roadmap
This roadmap reflects the project’s evolution from concept → MVP → scalable product.

### Completed
☑ Project Charter  
☑ Scope Statement  
☑ Requirements  
☑ Risk Register  
☑ Decision Log  
☑ Architecture Outline  
☑ Architecture Diagram  
☑ Inference Scaffold  
☑ API Scaffold  
☑ UI Scaffold  
☑ Logging Scaffold  

### In Progress
☐ Dataset Plan  
☐ Baseline Model (Azure Vision)  
☐ Inference API Wiring (connect to real model)  
☐ Minimal UI Wiring (JS → API)  
☐ Logging Integration (real events)  
☐ README Formatting & Presentation Cleanup (spacing, hierarchy, diagrams)

### Future
☐ Custom Model Training (multi‑brand, multi‑model)  
☐ Marketplace integration  
☐ Fraud‑detection heuristics  
☐ Feedback loop for continuous improvement  
☐ Deployment (Azure App Service / Static Web Apps)  
☐ Monitoring dashboards (Azure Monitor)  

For the full development roadmap, see [project_docs/08_Roadmap.md](project_docs/08_Roadmap.md).

10. Status
This is an early‑stage MVP.
A cleaned‑up version will be published next week.

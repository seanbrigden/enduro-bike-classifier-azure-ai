# Roadmap

This roadmap outlines the development path for the Enduro Bike Classifier project, moving from the current scaffolding to a functional MVP and beyond. It is structured around clear phases, dependencies, and deliverables.

---

## Phase 0 — Completed (Sprint Scaffolding)

- Project structure established  
- Inference scaffold created  
- API scaffold created  
- UI scaffold created  
- Logging scaffold created  
- Architecture outline completed  
- Architecture diagram added  
- Commit hygiene and verification completed  

This phase provides the foundation for all future development.

---

## Phase 1 — MVP Completion (Immediate Next Steps)

Minimal viable product: baseline model + working API + working UI.

### Baseline Model Integration
- Connect Azure Vision API to inference scaffold  
- Add real inference logic  
- Return prediction + confidence score  
- Add basic error handling  

### API Wiring
- Connect `/predict` to real inference  
- Add request validation (image type, size)  
- Add structured JSON response  

### UI Wiring
- Add JavaScript to send image → API  
- Display prediction + confidence  
- Add simple loading state  

### Logging
- Add real log_event calls  
- Log: request received, inference start, inference end, errors  
- Store logs locally (MVP)  

**Deliverable:** A working classifier that accepts an image and returns a prediction.

---

## Phase 2 — Model Improvement

Move beyond the baseline model.

### Dataset Prep
- Organize labeled images  
- Add dataset plan details  
- Upload to Azure Storage  

### Custom Model Training
- Train custom Azure Vision model  
- Evaluate accuracy  
- Document results  

### Inference Upgrade
- Replace baseline model with custom model  
- Add preprocessing if needed  
- Add confidence thresholding  

**Deliverable:** A more accurate classifier.

---

## Phase 3 — Production Hardening

Make the system stable, observable, and ready for deployment.

### Logging & Monitoring
- Add structured logging  
- Add correlation IDs  
- Integrate Azure Monitor  
- Add basic dashboards  

### Error Handling
- Add graceful API errors  
- Add UI error messages  
- Add retry logic for inference  

### Security
- Validate file types  
- Limit upload size  
- Add basic rate limiting  

**Deliverable:** A stable, observable MVP.

---

## Phase 4 — Deployment

Get the system live.

### Deployment Target
Choose one:
- Azure App Service (API)  
- Azure Static Web Apps (UI)  

### CI/CD
- GitHub Actions → Azure  
- Auto-deploy on main branch  

### Environment Setup
- Prod + Dev environments  
- Environment variables for keys  

**Deliverable:** A deployed, functioning classifier.

---

## Phase 5 — Future Enhancements

Optional but high-value improvements.

### Model
- Add more bike categories  
- Add explainability (saliency maps)  
- Add batch inference  

### UI
- Add drag-and-drop upload  
- Add history view  
- Add confidence visualization  

### API
- Add versioning  
- Add async inference  
- Add caching  

### Ops
- Add automated dataset ingestion  
- Add labeling tools  
- Add retraining pipeline  

---



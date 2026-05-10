# Architecture Outline

## High-Level Overview
A simple end-to-end system for classifying images of mountain bikes, starting with a baseline Azure Vision model and expanding later as needed. The architecture prioritizes clarity, maintainability, and minimal infrastructure for the MVP.

## Components
- **Dataset Storage:** Organized folder structure for labeled images.
- **Model Training:** Azure Vision baseline model for MVP; custom training later.
- **Inference API:** Lightweight API to accept images and return predictions.
- **Frontend UI:** Minimal interface for uploading an image and viewing results.
- **Logging & Monitoring:** Basic request logging for debugging and improvement.

## Data Flow
1. User uploads an image via the UI or API.
2. API receives the image and forwards it to the model.
3. Model performs inference and returns prediction + confidence score.
4. API returns the result to the user.
5. Logs are stored for later review and model improvement.

## Deployment Approach
- **Azure App Service** or **Azure Static Web Apps** for hosting.
- Minimal infrastructure to keep deployment simple and low-maintenance.
- Future flexibility to expand into more robust services if needed.

## Security & Privacy Considerations
- No personal data collected.
- Images processed only for classification.
- Logs anonymized and limited to operational data.

## Future Enhancements
- Custom model training for improved accuracy.
- Additional bike categories (trail, downhill, XC).
- More polished UI.
- Automated dataset ingestion and labeling tools.
- Model explainability (saliency maps, feature importance).

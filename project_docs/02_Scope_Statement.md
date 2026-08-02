# Scope Statement

## In Scope (MVP)

- Collect and curate a labelled dataset of two enduro frames, plus a negative
  class
- Train and evaluate a classifier using Azure Custom Vision
- Export the trained model for local inference
- Expose a prediction API accepting an image upload
- Provide a minimal UI for upload and result display
- Surface a retail link on a confirmed match
- Validate against held-out images and publish the results
- Document architecture, decisions, risks, and dataset

## In Scope (Stretch)

- Expand the negative class with hard examples and retrain
- Additional bike categories (trail, downhill, XC)
- Improved frontend experience
- Structured logging and basic analytics
- Model explainability (saliency maps) to identify which frame features drive
  predictions

## Out of Scope

- Production deployment and infrastructure (deferred by Decision 007)
- Authentication, rate limiting, monitoring
- Mobile application development
- Real-time video classification
- Automated large-scale dataset scraping
- Multi-model ensemble systems

## Assumptions

- Azure is the primary platform for model training
- GitHub is the source of truth for code and documentation
- Training data is sourced from publicly available product imagery

## Constraints

- Single contributor working in short increments
- Limited dataset availability for specific frame generations
- No local GPU; training performed in the Custom Vision portal
- Lightweight architecture with no production infrastructure

## Definition of Done (MVP)

- Local ONNX inference, API, and UI functioning end to end against real images
- Predictions returned with confidence scores and an explicit low-confidence
  response
- Retail link surfacing correctly on a confirmed match
- Held-out validation completed and results published, whatever they show
- PM artifacts consistent with the implemented system
- Clean repository structure

Deployment is explicitly excluded from the definition of done. Hosting the
pipeline does not change what the MVP demonstrates, and a live demonstration
dependent on a network round trip is less reliable than one that is not
(Decision 007).

## Status

Met. See `docs/validation-results.md` for what validation found, and the README
for known limitations.

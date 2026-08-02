# Architecture Outline

Describes the system as built. For decisions and their rationale see
`05_Decision_Log.md`.

## High-Level Overview

An end-to-end image classification system running entirely locally. A trained
Azure Custom Vision model is exported to ONNX and executed on the host machine —
there is no hosted prediction endpoint, no API key, and no network dependency at
inference time (Decision 009).

The architecture prioritises clarity and minimal infrastructure. Deployment is
deliberately out of MVP scope (Decision 007).

## Components

- **Model** — Azure Custom Vision, General (compact) domain, multiclass. Trained
  in the portal, exported to ONNX, committed to the repository at
  `src/model/enduro_classifier/`.
- **Inference** — `src/inference/baseline_inference.py`. Loads the ONNX model via
  `onnxruntime` once per process. Reads input dimensions from the model and
  preprocessing settings from `metadata_properties.json` rather than hardcoding
  them (Risk 10).
- **API** — `src/api/app.py`. FastAPI. Serves the UI at `/`, exposes `/predict`
  for image upload, and `/health`. Validates content type and upload size.
- **Interface** — `src/ui/index.html`. File upload, image preview, prediction
  and confidence display, conditional retailer link.
- **Logging** — `src/logging/logger.py`. Local event logging for predictions and
  errors.
- **Validation** — `data/golden/` holds held-out images; results are recorded in
  `docs/validation-results.md`.

## Data Flow

```
[User]
   ↓  uploads image
[UI: index.html]  ← served by FastAPI from the same origin
   ↓  POST /predict (multipart)
[API: app.py]
   ↓  validates type and size, passes raw bytes
[Inference: baseline_inference.py]
   ↓  resize → float32 → CHW → ONNX session
[Model: model.onnx]
   ↓  per-class probabilities
[Inference]
   ↓  applies confidence threshold, maps label → display name
[API]
   ↓  attaches retailer URL if the label has one and confidence clears
[UI displays result]
```

## Classes

Three: `santa_cruz_nomad`, `specialized_enduro`, `other`. The third exists
because a two-class model cannot express "neither" — every input is forced into
a known class (Decision 008, Risk 8).

## Confidence Handling

Predictions below a threshold return an explicit low-confidence response and
suppress the retailer link. This is an output control, not out-of-distribution
detection — it constrains what the system displays, it does not give the model
the ability to recognise unfamiliar input. Validation found it ineffective
against visually similar bikes (Risk 8).

## Security & Privacy

- No personal data collected; images are processed in memory for classification
  and not persisted.
- No API keys or secrets in the repository — a direct consequence of the local
  inference decision.
- Upload size capped; content type validated.
- Not production-hardened: no authentication, rate limiting, or monitoring.

## Future Enhancements

- Expand the negative class and retrain (`docs/sop-add-negative-class.md`)
- Multi-model coverage (`docs/dataset-spec.md` describes a candidate scope)
- Deployment to Azure App Service / Static Web Apps
- Structured logging and monitoring
- Model explainability (saliency maps) to show which frame features drive a
  prediction — directly relevant to the Nomad/Slash confusion

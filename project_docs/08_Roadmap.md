# Roadmap

Development path from scaffolding through MVP to a production-capable system.
Phase status reflects what has been executed and verified, not what has been
written (Decision 010).

---

## Phase 0 — Project Foundation ✅ Complete

- Project charter, scope statement, requirements
- Risk register, decision log, architecture outline, dataset plan
- Repository structure and commit hygiene

---

## Phase 1 — MVP ✅ Complete

**Model**
- Dataset collected and tagged in Azure Custom Vision
- Two-class model trained and evaluated
- Third `other` class added after out-of-distribution testing (Decision 008)
- Compact model exported to ONNX and committed (Decision 009)

**Inference**
- Local ONNX inference via `onnxruntime`
- Input dimensions and preprocessing read from the model and its metadata
- Confidence threshold with explicit low-confidence response
- Model loaded once per process

**API**
- `/predict` accepts image upload, returns label, confidence, per-class
  probabilities, and conditional retailer URL
- Content type and upload size validation
- UI served from the same origin
- `/health` endpoint

**UI**
- File upload with image preview
- Prediction and confidence display
- Conditional retailer link on a confirmed Nomad match

**Validation**
- Held-out image set established in `data/golden/`
- End-to-end test run and results published (`docs/validation-results.md`)

**Deliverable:** a working classifier that accepts an image and returns a
prediction, with documented performance against images it has never seen.

---

## Phase 2 — Model Improvement ⬜ Next

Validation showed the model reliably separates bikes from non-bikes but not
target frames from other full-suspension bikes. This phase addresses that.

- Expand `other` from 53 to ~120–150 images, weighted toward full-suspension
  trail and enduro bikes, prioritising other Santa Cruz models
- Add Nomad and Enduro images across varied angles and conditions
- Retrain, re-export, re-validate against the same held-out set
- Publish before/after comparison
- Evaluate whether the confidence threshold remains useful once the negative
  class is stronger

**Deliverable:** a classifier that rejects visually similar bikes rather than
confidently misidentifying them.

**Reference:** `docs/sop-add-negative-class.md`

---

## Phase 3 — Real-World Robustness ⬜

- Test against cluttered backgrounds, poor lighting, partial frames,
  non-drive-side photography, and bikes in motion
- Expand the held-out set to 20–30 images with a CSV manifest of expected labels
- Consider model explainability (saliency maps) to identify which frame features
  drive predictions

---

## Phase 4 — Production Hardening ⬜

- Structured logging with correlation IDs
- Graceful API and UI error handling
- Rate limiting and authentication
- Azure Monitor integration and basic dashboards

---

## Phase 5 — Deployment ⬜

- Azure App Service (API) and/or Static Web Apps (UI)
- GitHub Actions CI/CD
- Dev and production environments
- Model versioning — the current approach commits the ONNX file directly, which
  does not scale past a handful of iterations

---

## Phase 6 — Scale ⬜

- Multi-model, multi-brand coverage (`docs/dataset-spec.md` describes a
  candidate scope)
- Marketplace integration
- Fraud-detection heuristics — currently a hypothesis, not a demonstrated
  capability
- Feedback loop: capture low-confidence and corrected predictions as training
  data
- Automated dataset ingestion and labelling tools
- Batch and async inference

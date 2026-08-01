# Decision Log

A running record of key decisions, the context behind them, alternatives
considered, and the reasoning applied.

---

## Decision 001 — Define Scope and Architecture Before Writing Code
**Date:** 2026-05-09
**Context:** Solo project with a clear end goal but no fixed specification.
**Decision:** Produce the charter, scope statement, requirements, and
architecture outline before beginning implementation.
**Alternatives Considered:**
- Begin coding immediately and document retrospectively (rejected: on a project
  with an undefined boundary, this reliably produces rework)
**Rationale:** Defining the problem and the exclusions first keeps a solo project
from expanding indefinitely, and gives a reference point for judging whether
later work is in scope.

---

## Decision 002 — Deliver in Small, Independently Completable Increments
**Date:** 2026-05-09
**Context:** Limited contiguous development time.
**Decision:** Break work into units that can each be finished and verified within
a single session.
**Alternatives Considered:**
- Larger work blocks (rejected: increases the chance of leaving components
  half-finished, which is how untested code accumulates)
**Rationale:** Each increment ends in a known state. This proved directly
relevant later — see Decision 010.

---

## Decision 003 — Azure Custom Vision as the Model Platform
**Date:** 2026-05-09
**Context:** Needed a fast path from labelled images to a working classifier
without building a training pipeline.
**Decision:** Use Azure Custom Vision for training and evaluation.
**Alternatives Considered:**
- Custom model training with PyTorch or TensorFlow (rejected: substantially more
  setup for no MVP benefit at two classes)
- Off-the-shelf general image recognition (rejected: cannot distinguish specific
  bike models)
**Rationale:** Fastest route to a working end-to-end pipeline; built-in
evaluation metrics; supports export for local inference.

---

## Decision 004 — MVP Limited to Two Frames
**Date:** 2026-05-09
**Context:** Clear temptation to cover more brands and model years from the
outset.
**Decision:** Restrict the MVP to Santa Cruz Nomad V6 and Specialized Enduro
(2022+).
**Alternatives Considered:**
- Broad multi-brand coverage (rejected: dataset collection would dominate the
  timeline and delay any working demonstration)
**Rationale:** Two visually similar frames are sufficient to prove the pipeline
and are a harder test than two dissimilar ones. Breadth is a dataset problem,
not an architecture problem, and can be added later without redesign.
**Trade-off accepted:** A two-class model cannot express "neither" — see
Decision 008 and Risk 8.

---

## Decision 005 — Project Documentation Stored in the Repository
**Date:** 2026-05-09
**Context:** The project doubles as a portfolio piece.
**Decision:** Keep charter, scope, requirements, risks, decisions, and SOPs in
`project_docs/` and `docs/` alongside the code.
**Alternatives Considered:**
- Separate documentation tooling (rejected: fragments the project and adds a
  dependency for no benefit at this scale)
**Rationale:** Documentation stored next to the code it describes stays current
and gives a reviewer the reasoning alongside the implementation.

---

## Decision 006 — Repository Structure Kept Flat Until Needed
**Date:** 2026-05-09
**Context:** Early phase, minimal code.
**Decision:** Avoid premature package structure and abstraction layers.
**Rationale:** Structure added ahead of need becomes organisational debt.
Directories were introduced when the code actually required them.

---

## Decision 007 — Local Operation for MVP; Deployment Deferred
**Date:** 2026-05-10
**Context:** Deployment introduces hosting, environment configuration, and
secret management, none of which are needed to demonstrate the concept.
**Decision:** Run the API and UI locally for the MVP. Defer deployment to a
later roadmap phase.
**Alternatives Considered:**
- Deploy to Azure App Service immediately (rejected: adds failure modes and cost
  without changing what the MVP proves)
**Rationale:** The MVP's purpose is to demonstrate a working pipeline. Hosting
it does not make the pipeline more convincing, and a live demonstration
dependent on a network round trip is less reliable than one that isn't.

---

## Decision 008 — Confidence Threshold Rather Than Retraining, for MVP
**Date:** 2026-07-31
**Context:** Testing confirmed the two-class model returns high-confidence
predictions for images that are neither frame — a blank image returned 80.7%
confidence. The model has no mechanism to express uncertainty about class
membership itself.
**Decision:** Implement a confidence threshold that returns an explicit
low-confidence response and suppresses the retailer link, and document the
limitation openly.
**Alternatives Considered:**
- Add a third "other" class before the MVP milestone (rejected for this
  iteration: requires collecting and labelling ~50 negative images, retraining,
  and re-exporting; deferred rather than rushed at low quality)
- Ship with no guard (rejected: a confident wrong answer is the worst available
  failure mode, because it is indistinguishable from a correct one)
**Rationale:** The threshold captures most of the protective value at a fraction
of the cost, and is explicit about what it does not solve.
**Revisit:** Before any use beyond demonstration. Tracked as Risk 8.

---

## Decision 009 — Local ONNX Export Instead of a Hosted Prediction Endpoint
**Date:** 2026-07-31
**Context:** Custom Vision supports both a hosted REST prediction endpoint and a
downloadable compact model export.
**Decision:** Export the model to ONNX and run inference locally via
`onnxruntime`.
**Alternatives Considered:**
- Hosted Custom Vision endpoint (rejected: places API keys in a public
  repository, introduces a network dependency at demonstration time, and incurs
  per-call cost)
**Rationale:** No secrets to manage, no network dependency, no ongoing cost, and
the repository is self-contained for anyone reviewing it.
**Trade-off accepted:** A 44MB model file is committed to the repository, and
updating the model requires a re-export rather than a retrain in place.

---

## Decision 010 — Verification Required Before Marking Work Complete
**Date:** 2026-07-31
**Context:** A code review found that several components marked complete had
never been executed. Inference raised an exception on every call due to a
resolution mismatch with the exported model; the API and inference layers passed
incompatible types; and the retailer lookup referenced a label string that does
not exist. Project status had been tracked from development summaries rather
than from observed behaviour.
**Decision:** No item is marked complete until it has been executed end to end
against a real input and the output inspected.
**Alternatives Considered:**
- Continue tracking status from development summaries (rejected: this is what
  produced the inaccurate status)
**Rationale:** AI-assisted development produces plausible-looking code and
plausible-looking status reports through the same process. Neither is evidence
that something runs. Execution is the only reliable signal, and the cost of
checking is far lower than the cost of discovering it during a demonstration.

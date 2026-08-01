# Risk Register

Risks identified during development, with mitigations and residual exposure.
Risks are reviewed when project status changes materially.

---

## Risk 1: Dataset Quality and Consistency
**Description:** Training images vary in lighting, angle, resolution, and
background. Marketplace photography is typically lower quality than curated
product photography.
**Impact:** Reduced model accuracy, particularly on real-world images.
**Likelihood:** Medium
**Mitigation:** Manually curated dataset; documented image guidelines
(`docs/image-guidelines.md`); edge cases recorded rather than discarded.
**Residual Risk:** Medium — see Risk 4.

## Risk 2: Constrained Development Capacity
**Description:** Single-contributor project delivered in short increments.
**Impact:** Slower velocity; risk of partially finished components.
**Likelihood:** High
**Mitigation:** Tightly scoped MVP; work broken into independently completable
units; scope statement used as a guardrail.
**Residual Risk:** Low.

## Risk 3: Azure Service Configuration Complexity
**Description:** Azure AI services require account setup, domain selection, and
export configuration that can be misapplied without obvious symptoms.
**Impact:** Delays; incorrect model configuration reaching downstream code.
**Likelihood:** Medium
**Mitigation:** Start from the simplest viable configuration; document setup
steps as repeatable SOPs; validate after every configuration change.
**Residual Risk:** Low.

## Risk 4: Model Underperformance on Unseen Images
**Description:** The model may not generalise beyond its training distribution —
different lighting, cluttered backgrounds, partial frames, or non-drive-side
photography.
**Impact:** MVP appears unreliable in realistic conditions.
**Likelihood:** Medium
**Mitigation:** Held-out golden image set for validation before any demonstration
(`docs/sop-golden-images.md`); per-class metrics reviewed rather than overall
accuracy alone.
**Residual Risk:** Medium — the model has not yet been evaluated at scale against
real marketplace imagery.

## Risk 5: Scope Creep
**Description:** Adding categories, features, or infrastructure beyond MVP scope.
**Impact:** MVP never reaches a demonstrable state.
**Likelihood:** High
**Mitigation:** Scope statement defines exclusions explicitly; expansion ideas
recorded in the roadmap as future phases rather than acted on.
**Residual Risk:** Low.

## Risk 6: Deployment Complexity
**Description:** Hosting the API and UI introduces environment, networking, and
configuration work not required for local operation.
**Impact:** End-to-end demonstration delayed or unreliable.
**Likelihood:** Medium
**Mitigation:** MVP runs locally with no external dependencies; deployment
deferred to a later phase as an explicit decision (see Decision 007).
**Residual Risk:** Low for MVP; unaddressed for production.

## Risk 7: Dataset Licensing and Sourcing
**Description:** Images sourced from the web may carry usage restrictions.
**Impact:** Dataset may require rebuilding.
**Likelihood:** Low
**Mitigation:** Prefer self-collected and public-domain images; document sources
in the dataset plan.
**Residual Risk:** Low.

## Risk 8: Out-of-Distribution Inputs (Confident Misclassification)
**Description:** The two-class model assigns every input to one of its two known
frames. Images of other bikes, or of non-bikes entirely, are still classified —
often with high confidence.
**Impact:** High. A confidently wrong answer erodes trust in the system more than
an obvious failure does, because downstream processes and users treat a
high-confidence result as reliable. Verified during testing: a blank image
returned 80.7% confidence for one class.
**Likelihood:** High — in any realistic deployment, most uploads would be
neither frame.
**Mitigation:** Confidence threshold returns an explicit low-confidence response
instead of a label, and suppresses the retailer link. Planned: add a third
"other" class trained on negative examples
(`docs/sop-add-negative-class.md`).
**Residual Risk:** Medium. The threshold limits exposure but cannot eliminate it;
a misclassification above the threshold still surfaces as a confident answer.

## Risk 9: Generated Code Reporting False Completion
**Description:** AI-assisted development produced code and status entries
describing work as complete when the underlying code did not execute. Issues
found in review included a hardcoded input resolution that did not match the
exported model, a mismatched contract between the API and inference layers, and
a retailer lookup keyed to a label string absent from `labels.txt`.
**Impact:** High. Failures were silent or runtime-only, and project status
reflected generated summaries rather than tested behaviour.
**Likelihood:** High for AI-assisted work without an explicit verification step.
**Mitigation:** No item is marked complete until executed end to end against a
real input (see Decision 010). Golden-image validation before any demonstration.
**Residual Risk:** Low, once verification is applied consistently.

## Risk 10: Model Export Configuration Drift
**Description:** The exported model's expected input dimensions and preprocessing
are determined by its Custom Vision domain and can change on re-export.
Hardcoded preprocessing values break silently when the model changes.
**Impact:** Medium. Inference fails outright, or returns degraded results that
still appear plausible.
**Likelihood:** Medium — applies to every retrain-and-export cycle.
**Mitigation:** Inference reads input dimensions from the model at load time and
preprocessing settings from `metadata_properties.json` rather than hardcoding
them. Validation re-run after every export.
**Residual Risk:** Low.

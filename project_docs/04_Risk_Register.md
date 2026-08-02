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
**Description:** The model assigns visually similar bikes to a target frame with
high confidence. Validated: a Trek Slash returns santa_cruz_nomad at 0.873, a
road bike at 0.765. The `other` class separates bikes from non-bikes but not
target frames from other full-suspension bikes.
**Impact:** High. A confident wrong answer is indistinguishable from a correct
one to any downstream consumer, and in this build it surfaces a retail link for
the wrong product.
**Likelihood:** High — most real-world uploads would be neither target frame.
**Mitigation attempted:** A third `other` class was added (53 negative images),
which resolved the non-bike case but not the similar-bike case. A confidence
threshold was found to be ineffective: correct predictions scored 0.694–0.707
while incorrect predictions scored 0.765–0.873, so no threshold separates them.
**Planned mitigation:** Expand `other` to 120–150 images weighted toward
full-suspension trail and enduro bikes, particularly other Santa Cruz models.
**Residual Risk:** High, and accepted for the MVP. Documented rather than
mitigated. Not suitable for use beyond demonstration in its current state.

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

## Risk 11: Training Metrics Not Representative of Deployment Performance
**Description:** Custom Vision computes precision and recall by cross-validation
over the training images. These figures describe performance on the training
distribution, not on arbitrary user input. Validated: 89.3% reported versus 2 of
5 clean passes on held-out images.
**Impact:** High if acted on. A reported figure taken at face value would have
led to shipping a model that fails on the most common real-world case.
**Likelihood:** High — this applies to any model evaluated only by its training
platform's own metrics.
**Mitigation:** Held-out validation against independently sourced images before
any status claim (`docs/validation-results.md`). Re-run after every retrain
against the same image set for comparability.
**Residual Risk:** Low once held-out validation is standard practice.
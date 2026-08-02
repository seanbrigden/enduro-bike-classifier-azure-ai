# Validation Results

Held-out validation of the three-class model (Iteration 5), run against images
the model had never seen during training.

**Date:** 2026-08-01
**Model:** Iteration 5, General (compact) [S1], multiclass
**Confidence threshold:** 0.70

---

## Why this test exists

Custom Vision reports precision and recall computed by cross-validation over the
training images. Those numbers describe how the model performs on images drawn
from the same collection it learned from. They do not describe how it performs
on images from anywhere else.

This test uses five images sourced independently of the training set, chosen to
cover the cases a real user would produce: the two target frames, a visually
similar bike that is neither, a different bike category, and a non-bike.

## Reported metrics (Custom Vision, Iteration 5)

| Tag | Precision | Recall | A.P. | Images |
|---|---|---|---|---|
| santa_cruz_nomad | 100.0% | 88.9% | 100.0% | 42 |
| specialized_enduro | 87.5% | 87.5% | 95.5% | 38 |
| other | 83.3% | 90.9% | 96.0% | 53 |
| **Overall** | **89.3%** | **89.3%** | **96.3%** | **133** |

Note: the evaluation subset behind these figures is small — the per-tag values
resolve to fractions with denominators of roughly 8 to 11 — so each figure
carries a wide margin of error.

## Held-out results

| Image | Expected | Predicted | Confidence | Result |
|---|---|---|---|---|
| enduro01.png | specialized_enduro | specialized_enduro | 0.707 | Pass |
| nomad01.png | santa_cruz_nomad | santa_cruz_nomad | 0.694 | Correct, below threshold |
| other_not_a_bike.png | other | other | 0.937 | Pass |
| other_road_bike.png | other | santa_cruz_nomad | 0.765 | **Fail** |
| other_trek_slash.png | other | santa_cruz_nomad | 0.873 | **Fail** |

Both failures were reproduced independently using the Custom Vision portal's
Quick Test against the hosted iteration, confirming the behaviour originates in
the trained model rather than in local inference code.

## Findings

**1. Reported metrics substantially overstate real-world performance.**
89.3% overall precision and recall against 2 of 5 clean passes on held-out
images. The gap is not a defect in the metric — it is a consequence of
evaluating on images drawn from the training collection. Any accuracy figure
should be read alongside the question of what it was measured against.

**2. The `other` class learned bike-versus-non-bike, not Nomad-versus-other-bike.**
A non-bike image scored 0.937 for `other`, while a Trek Slash scored 0.873 for
`santa_cruz_nomad`. With 53 negative images covering the entire space of "not
these two frames," the model had sufficient signal for the coarse distinction
and insufficient signal for the fine one.

**3. The confidence threshold cannot separate these cases.**
Correct predictions scored 0.694 and 0.707. Incorrect predictions scored 0.765
and 0.873. The false positives score higher than the true positives, so no
threshold value admits the correct results while rejecting the incorrect ones.
Threshold tuning is not a mitigation for this failure mode.

**4. Distinguishing a Nomad V6 from a Trek Slash is fine-grained classification.**
The two frames share silhouette, travel category, and wheel size. Separating
them requires the model to key on linkage geometry and tube shaping. With 42
Nomad images and no visually similar negatives, nothing in training required it
to learn those features.

## Defect found during validation

Local inference initially returned near-identical probabilities for all five
images (approximately 0.58 / 0.31 / 0.10 regardless of input). Cause: the
preprocessing step divided pixel values by 255 in accordance with
`metadata_properties.json`, which reports
`Image.NominalPixelRange: Normalized_0_1`. The exported ONNX graph applies its
own scaling internally, so pre-scaled input collapsed the activations and the
output was driven by bias terms rather than by image content.

Fixed by passing raw 0–255 float values. Verified by measuring output spread
across structurally dissimilar images: 0.036 with the division applied, 0.178
without.

This defect was invisible to every metric reported by Custom Vision, since those
are computed server-side and never exercise local inference code.

## Next step

Expand the `other` class from 53 to approximately 120–150 images, weighted
toward full-suspension trail and enduro bikes. The highest-value additions are
other Santa Cruz models — Bronson, Megatower, Hightower, 5010, Nomad V5 — which
share the brand's design language and linkage, and therefore force the model to
learn what distinguishes a V6 specifically rather than what distinguishes a
Santa Cruz generally.

Procedure documented in `docs/sop-add-negative-class.md`. This test should be
re-run against the same five images after any retrain, so results remain
directly comparable.

## Reproducing this test

```
Get-ChildItem data\golden\* | ForEach-Object {
    Write-Host "`n=== $($_.Name) ==="
    python -m src.inference.test_inference $_.FullName
}
```

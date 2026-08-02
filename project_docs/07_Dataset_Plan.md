# Dataset Plan

Superseded by project_docs/07_Dataset_Plan.md

**Authoritative dataset document for this project.** Describes the dataset as
built, and the planned expansion. Supersedes `docs/dataset-plan.md`.
`docs/dataset-spec.md` describes a candidate future scope that is not
implemented.

---

## 1. Purpose

Define the data used to train the classifier, the standards applied, and the
gaps validation exposed.

## 2. Scope as Built

Three classes, model-level rather than brand-level:

| Class | Definition | Images |
|---|---|---|
| `santa_cruz_nomad` | Santa Cruz Nomad V6 | 42 |
| `specialized_enduro` | Specialized Enduro, 2022+ | 38 |
| `other` | Neither of the above — other bikes and non-bikes | 53 |
| | **Total** | **133** |

Two visually similar frames were chosen deliberately over two dissimilar ones:
a harder discrimination task is a more meaningful test of the pipeline
(Decision 004).

The `other` class was added after initial testing showed a two-class model
assigns every input to a known class regardless of content (Decision 008).

## 3. Out of Scope

- Earlier generations (Nomad V5 and prior, Enduro pre-2022)
- Other Santa Cruz VPP frames (Bronson, Megatower, Hightower, 5010)
- Other brands as named classes
- Frame material, suspension travel, or geometry metadata
- Object detection or segmentation — classification only

## 4. Sources

- Manufacturer product photography (Santa Cruz, Specialized, and others for the
  negative class)
- Bike review sites and retailer listings
- Press and product launch media

Sourcing follows `docs/image-guidelines.md`. Publicly available product imagery
only; no scraping of protected content.

## 5. Collection and Labelling

Images were collected manually and tagged in the Azure Custom Vision portal.
Custom Vision handles the train/validation split internally, so no local
train/val/test folder structure is maintained.

`data/golden/` holds held-out validation images sourced independently of the
training set. These are never uploaded to Custom Vision and are used only for
local end-to-end testing (`docs/validation-results.md`).

## 6. Quality Standards

- Full side profile preferred, drive side where available
- Bike occupies a substantial portion of the frame
- No rider obscuring the frame or linkage
- Suspension linkage visible where possible — it carries most of the
  distinguishing signal between similar frames
- No extreme lens distortion
- Duplicates and blurry images removed

## 7. Validated Gaps

Held-out testing exposed two dataset problems that the training metrics did not.

**The negative class is under-resourced for its diversity.** 53 images cover
"everything that is not one of two specific frames" — an enormous visual space.
The result: the model separates bikes from non-bikes reliably (a non-bike scored
0.937 for `other`) but not target frames from other full-suspension bikes (a
Trek Slash scored 0.873 for `santa_cruz_nomad`).

**Negatives lacked hard cases.** The negative set contained too few bikes
visually close to the target frames. Without them, nothing in training required
the model to learn linkage geometry or tube shaping — the features that actually
separate a Nomad V6 from a Slash.

## 8. Planned Expansion

Expand `other` from 53 to approximately 120–150 images, weighted toward
full-suspension trail and enduro bikes.

Priority order:

1. **Other Santa Cruz models** — Bronson, Megatower, Hightower, 5010, Nomad V5.
   Highest value: same brand design language and linkage, so they force the
   model to learn what distinguishes a V6 specifically.
2. **Other brands' enduro bikes** — Trek Slash, Giant Reign, YT Capra, Canyon
   Spectral, Norco Sight, Kona Process, Transition Sentinel.
3. **Other bike categories** — road, gravel, hardtail, e-bike.
4. **Non-bikes** — already adequately covered.

Additional Nomad and Enduro images across varied angles and conditions would
also help, since both target classes are currently thin.

Procedure: `docs/sop-add-negative-class.md`. The held-out test should be re-run
against the same images after every retrain so results stay comparable.

## 9. Risks

Dataset risks are tracked in `04_Risk_Register.md` — see Risk 1 (quality and
consistency), Risk 7 (licensing), Risk 8 (out-of-distribution inputs), and
Risk 11 (training metrics not representative of deployment performance).

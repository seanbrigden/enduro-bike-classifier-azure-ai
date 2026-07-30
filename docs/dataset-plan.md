Dataset Plan (Nomad V6 + Enduro MVP)
1. Objective
Build a small, clean, high‑signal dataset for a two‑class MVP classifier:

Santa Cruz Nomad V6

Specialized Enduro

The goal is not model performance optimization — the goal is to establish a repeatable, documented dataset pipeline that supports the baseline model, inference API, and UI.

2. Target Dataset Size
Because this is an MVP, the dataset is intentionally small:

Class	Target Images	Notes
Nomad V6	150–200	Mix of studio, catalog, and real‑world
Enduro	150–200	Same distribution as Nomad


Total: 300–400 images

This is enough for Azure Custom Vision to produce a baseline model and validate the end‑to‑end system.

3. Image Sources
To keep the dataset clean and legally safe, images will be sourced from:

Manufacturer websites (Santa Cruz, Specialized)

YouTube still frames (official bike reviews, manufacturer videos)

Marketplace listings (Pinkbike, MTBR, Facebook Marketplace)

Press kits / product launch media

User‑generated content (only when license/permissions allow)

All sources must comply with the rules defined in image-guidelines.md.

4. Collection Workflow
A simple, repeatable workflow:

Identify source

Manufacturer → highest quality

Marketplace → highest variability

YouTube → controlled lighting + angles

Download images

Save to data/raw/<class>/

Maintain original filenames

Apply quality filters

Remove images with heavy occlusion

Remove images with watermarks

Remove images with extreme clutter

Remove images where the frame is not visible

Normalize resolution

Resize to ~1024px longest side

Save to data/processed/<class>/

Create golden images

Select 10–15 per class

Store in data/golden/

Document counts

Update dataset-spec.md with final numbers

5. Train / Validation / Test Split
A simple, consistent split:

70% train

20% validation

10% test

This split is sufficient for Custom Vision and keeps the test set clean for baseline evaluation.

6. Labeling Strategy
Because this is a two‑class MVP:

No bounding boxes

No multi‑label classification

No parts‑based labeling

No segmentation

Each image receives one label only:

nomad_v6

enduro

This keeps the pipeline simple and reduces annotation overhead.

7. Baseline Evaluation Plan
After training the baseline model:

Evaluate using the test set only

Record:

Precision

Recall

Confusion matrix

Misclassified examples

Add results to sop-baseline-validation.md

The goal is not high accuracy — the goal is a working baseline that supports the inference API and UI.

8. Risks & Mitigations
Risk	Mitigation
Class imbalance	Enforce equal counts per class
Duplicate images	Use hashing to detect duplicates
Marketplace clutter	Apply strict filtering rules
Mislabeling	Use golden images as reference
Overfitting	Keep dataset diverse across sources


9. Next Steps After Dataset Completion
Once the dataset is ready:

Train baseline model in Azure Custom Vision

Export model + endpoint

Build inference script

Build inference API

Build minimal UI

Add logging + monitoring

Expand dataset (future phase)

10. Status
This dataset plan supports the narrowed MVP scope and will evolve as the system matures.

If you want, I can also generate:

a folder structure for data/

a collection checklist

a golden image selection SOP

a dataset README for the data/ folder

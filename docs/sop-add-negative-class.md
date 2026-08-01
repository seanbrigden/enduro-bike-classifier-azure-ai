# SOP — Adding an "Other" Class to the Classifier

**Purpose:** Give the model a legitimate place to put images that are neither a
Santa Cruz Nomad V6 nor a Specialized Enduro, so it stops being forced into a
confident wrong answer.

**Time required:** ~60–75 minutes, most of it collecting images.

**Prerequisites:** Access to the existing Custom Vision project at
[customvision.ai](https://www.customvision.ai) with the same Azure account used
to train the current model.

---

## Step 1 — Collect negative images (~40 minutes)

Target **50 images total**. More is better, but 50 is enough to work. Rough mix:

| Type | Count | Examples |
|---|---|---|
| Other enduro / trail bikes | 20 | Trek Slash, Giant Reign, YT Capra, Canyon Spectral, Norco Sight, Kona Process |
| Other bike categories | 10 | Road, gravel, hardtail, e-bike, kids' bike |
| Bike parts and close-ups | 8 | Wheels, cranks, forks, a frame detail with no full bike |
| Non-bike images | 12 | Cars, people, rooms, landscapes, product boxes |

Two things matter more than the exact split:

- **Include other full-suspension enduro bikes.** These are the hard cases. A
  Trek Slash looks far more like a Nomad than a landscape does, so these are what
  actually teach the model the boundary. If you only add photos of dogs and
  parking lots, the model learns "bike vs not-bike," which is not the problem
  you have.
- **Match the style of your training images.** Similar angles, similar
  backgrounds, similar resolution. If your Nomad and Enduro photos are clean
  product shots and your negatives are all blurry phone snaps, the model may
  learn to separate on image quality rather than on the bike.

Save them into `data/raw/other/`.

---

## Step 2 — Upload and tag in Custom Vision (~10 minutes)

1. Go to [customvision.ai](https://www.customvision.ai) and sign in.
2. Open your existing project — **do not create a new one**. You want the
   existing Nomad and Enduro images to stay exactly as they are.
3. Click **Add images**.
4. Select all 50 negative images at once.
5. In the tag box, type `other` and press Enter to create the tag.
6. Click **Upload**.

Once uploaded, confirm the left sidebar shows three tags: `santa_cruz_nomad`,
`specialized_enduro`, and `other`, each with a sensible image count.

> **Note on the built-in "Negative" tag:** Custom Vision offers a special
> Negative tag. It works, but the exported `labels.txt` will then contain
> `Negative`, and you'd need to match that string in the code. Using a normal
> tag named `other` keeps everything lowercase and consistent. Either is fine —
> just be consistent with whatever appears in `labels.txt` after export.

---

## Step 3 — Retrain (~5 minutes)

1. Click **Train** (top right).
2. Choose **Quick Training**.
3. Wait. Typically 2–10 minutes for a dataset this size.

When it finishes you land on the Performance tab for the new iteration.

---

## Step 4 — Check the results before you export (~5 minutes)

On the Performance tab, look at the per-tag breakdown, not just the overall
numbers.

- **Precision** — when it says `other`, how often is it right?
- **Recall** — of all the actual `other` images, how many did it catch?

What you want to see is that `other` recall is decent (roughly 0.80+) and that
Nomad and Enduro precision has not collapsed. Some drop in the two original
classes is normal and expected — the task genuinely got harder.

**Write these numbers down.** They replace the `XX%` placeholders in your README.

If `other` recall is poor, the usual cause is too few hard negatives. Add more
full-suspension enduro bikes specifically and retrain.

---

## Step 5 — Export the model (~5 minutes)

1. On the Performance tab for the new iteration, click **Export**.
2. Choose **ONNX**.
3. Download the `.zip`.

> **If the Export button isn't there:** your project is on a non-compact domain.
> Go to **Settings**, change the domain to **General (compact)**, save, and
> retrain. Only compact domains can be exported for local use.

---

## Step 6 — Swap the files into the repo (~2 minutes)

Unzip the download. Copy these three files into
`src/model/enduro_classifier/`, overwriting what's there:

- `model.onnx`
- `labels.txt`
- `metadata_properties.json`

Copy all three together. They belong to each other — a new `model.onnx` with the
old `labels.txt` will map predictions to the wrong names, which is exactly the
kind of failure that looks like it's working.

Open `labels.txt` and confirm it now has three lines.

---

## Step 7 — Update the display names (~1 minute)

In `src/inference/baseline_inference.py`, add the third entry, matching the
exact string from `labels.txt`:

```python
DISPLAY_NAMES = {
    "santa_cruz_nomad": "Santa Cruz Nomad V6",
    "specialized_enduro": "Specialized Enduro",
    "other": "Not a Nomad or an Enduro",
}
```

Nothing else needs to change. The inference code reads the label list and the
input dimensions from the model itself, so a different number of classes or a
different input size is handled automatically. `RETAILER_LINKS` is keyed by raw
label, so no Backcountry link appears for `other` without any extra logic.

---

## Step 8 — Validate (~10 minutes)

From the repo root:

```bash
python -m src.inference.test_inference data/golden/<a_known_nomad>.jpg
```

Run through this checklist:

- [ ] A known Nomad returns `santa_cruz_nomad` with high confidence
- [ ] A known Enduro returns `specialized_enduro` with high confidence
- [ ] A different mountain bike (one **not** used in training) returns `other`
- [ ] A non-bike image returns `other`
- [ ] Probabilities sum to approximately 1.0

Then start the app and click through the UI once:

```bash
python -m uvicorn src.api.app:app --reload
```

- [ ] Nomad upload shows the Backcountry banner
- [ ] Enduro upload shows no banner
- [ ] `other` upload shows no banner and no bike name

---

## Step 9 — Reconsider the threshold

With three classes, the confidence threshold in `baseline_inference.py` is doing
less work — the model can now say `other` on its own. You may want to lower
`CONFIDENCE_THRESHOLD` from 0.85 back toward 0.70 so genuine matches aren't
rejected unnecessarily. Test against your golden images and pick the number that
holds up, rather than guessing.

---

## Step 10 — Update the documentation

- README: replace the `XX%` placeholders with the real per-class numbers from
  Step 4, and revise the Known Limitations section — the "two-class model
  cannot express neither" limitation is now largely resolved.
- `project_docs/04_Risk_Register.md`: update Risk 9 to reflect the mitigation
  actually shipping, and lower the residual risk.
- `project_docs/05_Decision_Log.md`: add an entry recording that the third class
  was added, with the before/after numbers.

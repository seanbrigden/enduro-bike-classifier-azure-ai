# Requirements

## Functional Requirements

- The system must accept an uploaded image via a browser interface.
- The system must classify the image into one of three categories: Santa Cruz
  Nomad V6, Specialized Enduro (2022+), or other.
- The system must return a confidence score with each prediction.
- The system must return an explicit low-confidence response, rather than a
  class name, when confidence falls below a configured threshold.
- The system must surface a retail link when a target frame is identified above
  the confidence threshold, and suppress it otherwise.
- The system must log predictions and errors locally for review.
- The system must expose an API endpoint accepting an image via POST.
- The UI must allow image upload and display the result with its confidence
  score.

## Non-Functional Requirements

- Predictions should return within 2–3 seconds on a standard laptop.
- Inference must run locally with no network dependency and no API keys in the
  repository.
- The system should be capable of deployment to standard Azure services in a
  later phase, though deployment is out of MVP scope.
- The codebase should follow a clean, modular folder structure.
- Documentation must be maintained in the repository and reflect the system as
  built.
- The UI should be simple and functional; visual polish is not a requirement.

## Data Requirements

- Training images must cover both target frames and a representative negative
  class.
- Images must be of sufficient quality and resolution for training.
- The dataset must include variation in angle, lighting, and background.
- Training images are uploaded and tagged in the Azure Custom Vision portal,
  which manages storage and the train/validation split. No local training
  dataset structure is maintained in the repository.
- A held-out validation set is maintained locally at `data/golden/`, sourced
  independently of the training data and never uploaded to Custom Vision.
- Dataset scope, standards, and known gaps are documented in
  `07_Dataset_Plan.md`.

## Model Requirements

- The model must be trained using Azure Custom Vision.
- The model must support single-image inference.
- The model must be exported in a compact format (ONNX) for local execution.
- Inference code must read input dimensions and preprocessing settings from the
  exported model and its metadata rather than hardcoding them, so a re-export at
  different settings does not silently break inference.
- Training steps must be documented as a repeatable procedure. Training is
  performed through the Custom Vision portal, so reproducibility is achieved
  through documented SOPs (`docs/sop-add-negative-class.md`) rather than a
  repository-hosted training pipeline.

## API Requirements

- The API must accept an image file via POST.
- The API must validate content type and reject uploads above a size limit.
- The API must return the prediction, confidence, and per-class probabilities.
- The API must return a retail URL only when one applies and confidence clears
  the threshold.
- The API must handle invalid or corrupted images gracefully with an
  appropriate status code.
- The API must serve the UI from the same origin.

## UI Requirements

- The UI must allow image upload.
- The UI must display the prediction and confidence clearly.
- The UI must display the retail link only when returned by the API.
- The UI must surface API errors to the user rather than failing silently.

## Constraints

- Single contributor working in short increments.
- Azure as the platform for model training.
- No local GPU.
- Lightweight architecture with no production infrastructure.

## Acceptance Criteria

- A user can upload an image through the browser and receive a classification
  with a confidence score.
- The API returns valid predictions and handles invalid input gracefully.
- The retail link appears on a confirmed target match and is suppressed
  otherwise.
- Held-out validation has been executed and its results published.
- Documentation is consistent with the implemented system.

## Verification

Acceptance is established by execution against real images, not by code review
or generated status reports (Decision 010). Results are recorded in
`docs/validation-results.md`.

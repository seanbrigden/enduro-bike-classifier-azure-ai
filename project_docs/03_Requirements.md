# Requirements

## Functional Requirements (What the system must do)
- The system must accept an uploaded image of a mountain bike.
- The system must classify whether the bike is an enduro bike.
- The system must return a confidence score with each prediction.
- The system must log predictions for later review.
- The system must expose an API endpoint for programmatic access.
- The UI must allow a user to upload an image and view the result.
- The dataset tools must support adding, labeling, and cleaning images.
- The training pipeline must be reproducible and documented.

## Non-Functional Requirements (How the system must behave)
- The system should respond to predictions within 2–3 seconds.
- The model should achieve baseline accuracy suitable for MVP (to be defined).
- The system should be deployable on Azure using standard services.
- The codebase should follow a clean, modular folder structure.
- Documentation should be maintained in the repository.
- The UI should be simple, minimal, and mobile-friendly.

## Data Requirements
- A dataset of enduro mountain bike images (minimum viable size TBD).
- Images should be high enough quality for model training.
- Dataset must include variations in angle, lighting, and bike models.
- Dataset must be stored in a structured folder format.
- Metadata should include labels and any preprocessing notes.

## Model Requirements
- Baseline model must be trained using Azure AI services.
- Model must support single-image inference.
- Model must be exportable for deployment (ONNX or Azure-native format).
- Model training steps must be documented and reproducible.

## API Requirements
- API must accept an image file via POST.
- API must return prediction + confidence score.
- API must handle invalid or corrupted images gracefully.
- API must log requests for debugging and improvement.

## UI Requirements
- UI must allow image upload from desktop and mobile.
- UI must display prediction results clearly.
- UI must show confidence score.
- UI should be minimal and easy to navigate.

## Constraints (Inherited from Scope)
- 30 minutes per day until AI-900 is complete.
- Solo developer workflow.
- Azure as primary cloud platform.
- Lightweight architecture until post-exam.

## Acceptance Criteria
- User can upload an image and receive a classification.
- API returns valid predictions with confidence scores.
- Model training pipeline runs end-to-end.
- Documentation is complete and up to date.
- Repo structure is clean and professional.

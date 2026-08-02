# Project Charter

## Problem Statement

Marketplace bike listings are frequently miscategorised or misdescribed, which
degrades search relevance, seller visibility, and buyer trust, and creates
manual verification work for support teams. This project tests whether image
classification could make categorisation a system property rather than
something dependent on the seller getting it right.

## Vision

A constrained, fully documented AI product case study: a working end-to-end
pipeline, honest evaluation of what it can and cannot do, and the product
artifacts that would surround it in a commercial setting.

## Objectives

- Build a labelled dataset of two visually similar enduro frames
- Train and evaluate a classifier using Azure AI services
- Run inference end to end from a browser upload to a displayed prediction
- Connect a confirmed match to a retail purchase path
- Validate against images outside the training set and publish the results
- Maintain PM artifacts that reflect the system as built

## Success Criteria

- A working classifier reachable through a browser interface
- Predictions returned with confidence scores and an explicit low-confidence
  response
- Held-out validation performed and results documented, whatever they show
- Documentation consistent with the implemented system
- Clean, navigable repository structure

## Out of Scope

Production deployment, authentication, monitoring, multi-brand coverage, and
mobile applications. See `02_Scope_Statement.md`.

## Commercial Considerations (Exploratory)

Outside MVP scope, but the underlying capability has adjacent applications
worth noting. These are hypotheses, not demonstrated results.

- **Marketplace listing accuracy** — automated categorisation at upload,
  reducing manual verification and improving search relevance
- **Merchandising** — connecting identified products to purchase paths, the
  mechanism demonstrated in this MVP
- **Bike park analytics** — aggregated, anonymised model identification could
  inform rental fleet planning, parts inventory, and seasonal demand forecasting
- **Retail insights** — anonymised model distribution data to guide stocking
  decisions
- **Manufacturer feedback** — with appropriate permissions and ethical data
  handling, aggregated usage trends

Fraud and counterfeit detection are frequently cited for this class of
capability. A two-class classifier does not evidence them, and validation
showed the model cannot reliably distinguish visually similar frames — the
precise capability those applications would require.

## Constraints

- Single contributor, delivered in short increments
- Dataset limited to publicly available product imagery
- No local GPU; training performed in Azure Custom Vision
- Lightweight architecture, no production infrastructure

## Governance

Project decisions are recorded in `05_Decision_Log.md` with alternatives
considered. Risks are tracked in `04_Risk_Register.md`. No component is marked
complete until it has been executed end to end against a real input
(Decision 010).

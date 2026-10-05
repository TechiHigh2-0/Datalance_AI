# DataLens AI — Risks and Engineering Decisions

## Decision 1 — Streamlit instead of React

Reason:
The hackathon has a short build window. Streamlit reduces frontend/backend integration work.

---

## Decision 2 — No Database

Reason:
The MVP does not require persistence. A database would add complexity without improving the core demo.

---

## Decision 3 — Pandas before Gemma

Reason:
Numerical computation should be deterministic.

This reduces hallucination risk and makes the AI layer easier to trust.

---

## Decision 4 — Evidence-based prompts

Reason:
The model should explain verified facts instead of inventing calculations.

---

## Risk 1 — local inference performance

Mitigation:
- minimize API calls,
- compute locally,
- cache AI results where useful,
- avoid unnecessary repeated requests.

---

## Risk 2 — Ollama unavailable

Mitigation:
The core data analysis and visualization features work without AI.

---

## Risk 3 — AI hallucination

Mitigation:
- evidence object,
- strict system prompt,
- no raw unrestricted dataset reasoning for numerical claims,
- visible evidence in UI.

---

## Risk 4 — Scope creep

Mitigation:
P0/P1/P2 feature classification.

If P0 is not stable, P1/P2 work stops.

---

## Risk 5 — Demo dataset failure

Mitigation:
Include a deterministic local sample dataset in the repository.

---

## Risk 6 — Secrets committed to Git

Mitigation:
- `.env`
- `.gitignore`
- `.env.example`
- pre-submission secret scan

---

## Risk 7 — Overclaiming AI capabilities

Mitigation:
Use careful language such as:
- "suggests"
- "may indicate"
- "worth investigating"

Avoid unsupported causal statements.

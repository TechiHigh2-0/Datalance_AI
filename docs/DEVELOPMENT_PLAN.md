# DataLens AI — Development Plan

## Principle

Build the smallest complete product first.

Do not start with polish or optional AI features.

---

## Phase 0 — Environment

- [ ] Python installed
- [ ] Git installed
- [ ] Antigravity ready
- [ ] Google AI Studio access
- [ ] Ollama installed and running
- [ ] Gemma 4 model downloaded locally
- [ ] GitHub repository created

---

## Phase 1 — Project Skeleton

- [ ] Create repository structure
- [ ] Create virtual environment
- [ ] Create requirements.txt
- [ ] Create Streamlit entry point
- [ ] Add .gitignore
- [ ] Add .env.example

Acceptance:

`streamlit run app.py` opens successfully.

---

## Phase 2 — File Loading

- [ ] CSV upload
- [ ] XLSX upload
- [ ] Dataframe preview
- [ ] Invalid file handling

Acceptance:

A sample CSV and XLSX load correctly.

---

## Phase 3 — Dataset Profiler

- [ ] Row count
- [ ] Column count
- [ ] Data types
- [ ] Missing values
- [ ] Missing percentages
- [ ] Duplicate rows
- [ ] Unique values

Acceptance:

The overview and data-quality table are correct.

---

## Phase 4 — Statistics

- [ ] Numerical summary
- [ ] Aggregations
- [ ] Date detection
- [ ] Basic trend calculations

Acceptance:

Known sample-dataset values match expected values.

---

## Phase 5 — Visualization

- [ ] Time-series chart
- [ ] Categorical comparison
- [ ] Distribution
- [ ] Scatter where applicable

Acceptance:

Charts render correctly and labels are understandable.

---

## Phase 6 — Gemma Integration

- [ ] Install Google GenAI SDK
- [ ] Read GEMINI_API_KEY from environment
- [ ] Configurable model name
- [ ] Basic API call
- [ ] Error handling
- [ ] AI summary

Acceptance:

Local Gemma 4 through Ollama produces a grounded summary from known evidence.

---

## Phase 7 — Ask Your Data

- [ ] Question input
- [ ] Identify relevant analytical context
- [ ] Compute evidence
- [ ] Send evidence to Gemma
- [ ] Display answer + evidence

Acceptance:

At least five demo questions work.

---

## Phase 8 — UI Polish

- [ ] Consistent title
- [ ] Metric cards
- [ ] Clear sections
- [ ] Loading states
- [ ] Error states
- [ ] Sample dataset button

---

## Phase 9 — Optional Multimodal Feature

Only after the core app is stable:

- [ ] Dashboard screenshot upload
- [ ] Gemma image analysis
- [ ] Visual insight output

---

## Phase 10 — Open Source Submission

- [ ] README
- [ ] License
- [ ] CONTRIBUTING
- [ ] AI disclosure
- [ ] Screenshots
- [ ] Setup instructions
- [ ] Demo instructions
- [ ] Public GitHub repository

---

## Phase 11 — Freeze

Once the core demo works:

DO NOT add new major features.

Only fix:

- bugs,
- broken UI,
- README,
- demo flow,
- submission details.

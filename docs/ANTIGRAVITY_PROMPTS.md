# DataLens AI — Antigravity Development Prompts

Use these prompts sequentially. Do not ask Antigravity to regenerate the entire project after each step.

---

## Prompt 1 — Project Skeleton

Create a Python Streamlit project named DataLens AI.

Use this structure:

[PASTE PROJECT STRUCTURE FROM TECHNICAL_DESIGN.md]

Requirements:
- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- openpyxl
- google-genai
- python-dotenv

Do not implement AI yet.

Create:
- app.py
- requirements.txt
- .gitignore
- .env.example
- package/module folders
- a clean Streamlit shell

Run the application and fix startup errors.

---

## Prompt 2 — File Loading

Implement CSV and XLSX upload.

Requirements:
- validate uploaded files,
- load with Pandas,
- show a dataframe preview,
- handle invalid files gracefully,
- keep the UI simple.

Do not add Gemma/Ollama yet.

Test with the included sample dataset.

---

## Prompt 3 — Data Profiler

Implement:
- rows
- columns
- data types
- missing values
- missing percentage
- duplicates
- unique values

Keep calculations deterministic.

Add unit tests for the profiler.

---

## Prompt 4 — Statistics

Implement numerical statistics and useful grouped aggregations.

Support:
- count
- mean
- median
- min
- max
- standard deviation
- sums by category
- date-based trends when a date column exists

Do not use an LLM for calculations.

---

## Prompt 5 — Visualizations

Implement a small chart recommendation layer.

Rules:
- date + numeric → line chart
- category + numeric → bar chart
- numeric + numeric → scatter plot
- categorical distribution → bar chart

Use Plotly.

Do not generate more than 5 primary charts.

---

## Prompt 6 — Gemma Integration

Integrate Gemma 4 through the Google GenAI Python SDK.

Read:
GEMINI_API_KEY

Optional:
GEMMA_MODEL

Default:
gemma-4-26b-a4b-it

Add:
- connection error handling
- empty response handling
- Ollama connection/model timeout and error handling

Do not require or expose any cloud API key.

---

## Prompt 7 — Grounded Insights

Build an evidence object from Pandas results.

Send the evidence to Gemma.

Implement the system rules from AI_SPEC.md:
- never invent numbers,
- use only supplied evidence,
- distinguish observations and recommendations.

Display:
- summary
- key insights
- recommendation

---

## Prompt 8 — Ask Your Data

Implement a natural-language question interface.

For the MVP:
1. identify the relevant available metrics/columns,
2. calculate useful evidence with Pandas,
3. send evidence plus question to Gemma,
4. return:
   - direct answer,
   - evidence,
   - explanation,
   - optional next step.

Do not send the entire dataframe unnecessarily.

---

## Prompt 9 — UI Polish

Improve the Streamlit interface without changing functionality.

Requirements:
- clean hierarchy
- metric cards
- clear section titles
- loading states
- useful empty states
- clear errors
- responsive layout
- no excessive animation

Do not add new major features.

---

## Prompt 10 — Final QA

Read PRD.md, TECHNICAL_DESIGN.md and TEST_PLAN.md.

Audit the implementation against the requirements.

Fix only:
- bugs,
- missing P0 functionality,
- security issues,
- documentation gaps.

Do not introduce new architecture.

---

## Prompt 11 — README and Open Source

Generate the final README using README_TEMPLATE.md.

Include:
- setup
- architecture
- screenshots
- demo instructions
- AI disclosure
- license

Make sure no secret/API key is present.

---

## Prompt 12 — Optional Multimodal Feature

Only execute if all P0 features are stable.

Add dashboard screenshot upload and local Gemma 4 visual interpretation through Ollama, only if the installed model/runtime supports the required image input.

Keep this feature isolated so it can be disabled without affecting the core application.

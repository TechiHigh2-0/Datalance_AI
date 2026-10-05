# DataLens AI — Technical Design

## 1. Architecture

```text
Browser
   |
   v
Streamlit UI
   |
   +----------------------+
   |                      |
   v                      v
Pandas/Data Engine     Plotly
   |
   v
Verified Analytical Context
   |
   v
Gemma 4 via Ollama (local inference)
   |
   v
AI Insights / Ask Your Data
```

The application intentionally avoids a separate backend and database.

---

## 2. Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| UI | Streamlit | Web application |
| Language | Python | Main implementation |
| Data | Pandas | Dataset processing |
| Numerical | NumPy | Numerical operations |
| Charts | Plotly | Interactive visualization |
| Excel | openpyxl | XLSX parsing |
| AI runtime | Ollama | Local Gemma 4 inference |
| AI | Gemma 4 | Interpretation and reasoning |
| Config | python-dotenv | Local environment configuration |
| Version control | Git/GitHub | Open-source repository |

---

## 3. Model Strategy

Use Gemma 4 through the Gemini API.

Preferred initial model:

`gemma-4-26b-a4b-it`

Keep the model identifier configurable through application configuration so it can be changed without rewriting the application.

The application should not depend on local model hosting for the hackathon MVP.

---

## 4. Separation of Responsibilities

### Pandas

Responsible for facts:

- row counts,
- missing values,
- duplicates,
- grouping,
- aggregation,
- statistics,
- trends.

### Plotly

Responsible for visual presentation.

### Gemma 4

Responsible for:

- interpreting verified results,
- summarizing findings,
- answering natural-language questions,
- turning evidence into understandable explanations,
- optional screenshot interpretation.

---

## 5. Evidence Object

The AI layer should receive a compact structured object rather than the entire dataframe whenever possible.

Example:

```json
{
  "dataset": {
    "rows": 10482,
    "columns": 8
  },
  "quality": {
    "missing_values": 127,
    "duplicate_rows": 14
  },
  "metrics": {
    "total_revenue": 1245000,
    "average_revenue": 2340
  },
  "trends": {
    "February": 170000,
    "March": 110000
  },
  "top_category": "Electronics"
}
```

This reduces token usage and lowers the risk of unsupported model claims.

---

## 6. Question Answering Flow

```text
User Question
     |
     v
Question interpretation
     |
     v
Identify relevant columns/metrics
     |
     v
Pandas calculations
     |
     v
Evidence object
     |
     v
Gemma 4
     |
     v
Grounded explanation
```

The model should not be allowed to fabricate a calculation that can be performed deterministically by Python.

---

## 7. Suggested Package Structure

```text
datalens-ai/
├── app.py
├── analyzer/
│   ├── __init__.py
│   ├── profiler.py
│   ├── statistics.py
│   └── insights.py
├── visualization/
│   ├── __init__.py
│   └── charts.py
├── ai/
│   ├── __init__.py
│   ├── gemma.py
│   └── prompts.py
├── utils/
│   ├── __init__.py
│   └── file_loader.py
├── data/
│   └── sample_sales.csv
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

---

## 8. Environment Variables

Required:

```text
GEMINI_API_KEY=
```

Optional:

```text
GEMMA_MODEL=gemma-4-26b-a4b-it
```

The real `.env` file must be ignored by Git.

---

## 9. Failure Strategy

If Ollama/Gemma is unavailable:

- continue showing dataset profile,
- continue showing statistics,
- continue showing charts,
- show a clear AI-unavailable message.

AI failure must not crash the entire application.

---

## 10. API Usage Strategy

Keep API calls intentionally low.

Typical session:

- dataset upload: 0 AI calls,
- AI summary: 1 call,
- each user question: 1 call,
- optional image analysis: 1 call.

The free tier has limits, so the app should avoid unnecessary calls.

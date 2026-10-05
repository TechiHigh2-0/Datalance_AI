# DataLens AI

> Turn raw data into clear decisions.

DataLens AI is a free AI-powered data analyst that transforms CSV and Excel datasets into data-quality reports, visualizations, and evidence-backed insights using Gemma 4 locally through Ollama.

## Features

- CSV/XLSX upload
- Dataset profiling
- Missing-value and duplicate detection
- Statistical analysis
- Automatic visualizations
- AI-generated insights
- Natural-language "Ask Your Data"
- Optional multimodal dashboard analysis

## Architecture

```text
CSV/XLSX
   ↓
Pandas
   ↓
Verified analytical evidence
   ↓
Gemma 4
   ↓
AI explanation
```

Pandas is responsible for deterministic calculations. Gemma 4 is responsible for interpretation and natural-language explanation.

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- openpyxl
- Google GenAI SDK
- Gemma 4

## Setup

### 1. Clone

```bash
git clone <REPOSITORY_URL>
cd datalens-ai
```

### 2. Create environment

```bash
python -m venv .venv
```

Activate it for your operating system.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API key

Create `.env`:

```text
GEMINI_API_KEY=your_key_here
GEMMA_MODEL=gemma-4-26b-a4b-it
```

Never commit `.env`.

### 5. Run

```bash
streamlit run app.py
```

## Demo

Use the included sample dataset:

```text
data/sample_sales.csv
```

Suggested questions:

- Why did revenue fall in March?
- Which category performs best?
- Which region should I investigate?
- What are the biggest changes?
- Are there unusual values?

## AI Disclosure

AI coding assistants were used during development as permitted by the hackathon rules.

Gemma 4 is used locally through Ollama at runtime for natural-language data interpretation and insight generation. No cloud AI API key is required.

## Open Source

This project is released under the Apache License 2.0.

## Hackathon

Built for Hacktoberfest Hack Day Kolkata × GDGoC GCELT.

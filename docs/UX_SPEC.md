# DataLens AI — UX Specification

## Design Goal

The interface should feel like a lightweight AI analyst rather than a complicated BI platform.

## Main Navigation

Keep navigation minimal:

1. Overview
2. Data Quality
3. Visual Analysis
4. AI Insights
5. Ask Your Data

A single-page Streamlit dashboard is acceptable for the MVP.

---

## Header

```text
DataLens AI
Turn raw data into clear decisions.
```

Show the uploaded filename and an option to replace the dataset.

---

## Overview

Four primary metric cards:

- Rows
- Columns
- Missing Values
- Duplicate Rows

---

## Data Quality

Display a table:

| Column | Type | Missing | Missing % | Unique |
|---|---|---:|---:|---:|

Use clear status indicators for warnings.

---

## Visual Analysis

Show 3–5 useful charts maximum.

Avoid generating charts just to fill space.

Each chart should answer a useful question such as:

- How is the metric changing?
- Which category is strongest?
- Which region contributes most?
- Are two variables related?

---

## AI Insights

Use insight cards:

### Key Trend

What changed?

### Top Performer

Which category/region/product leads?

### Potential Anomaly

What looks unusual?

### Recommendation

What should the user investigate next?

All AI-generated claims should be traceable to computed evidence.

---

## Ask Your Data

Primary interaction:

```text
Ask something about your dataset...
```

Example questions:

- Why did revenue fall in March?
- Which category performs best?
- Which region should I investigate?
- Are there unusual values?
- What are the biggest changes?

Answer layout:

1. Direct answer
2. Evidence
3. Explanation
4. Optional follow-up

---

## Empty State

Before upload:

```text
Upload a CSV or Excel file to begin.
```

Provide a button to load the included sample dataset.

---

## Error State

Never display raw stack traces to users.

Instead:

```text
We couldn't read this file.

Check that it is a valid CSV/XLSX file and try again.
```

For API errors:

```text
The dataset analysis is available, but AI insights are temporarily unavailable.
```

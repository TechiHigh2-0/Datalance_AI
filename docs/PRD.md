# DataLens AI — Product Requirements Document (PRD)

**Version:** 1.0  
**Status:** Hackathon Build Specification  
**Project:** DataLens AI  
**Event:** Hacktoberfest Hack Day Kolkata × GDGoC GCELT  
**Primary model:** Gemma 4  
**Target build window:** One-day hackathon / approximately 5-hour hacking period

---

## 1. Product Summary

DataLens AI is a free, AI-powered data analyst that turns CSV and Excel datasets into understandable, evidence-backed insights.

The product combines deterministic data analysis with Gemma 4 running locally through Ollama:

- Python/Pandas calculates facts and statistics.
- Plotly renders interactive visualizations.
- Gemma 4 interprets verified analytical context and explains findings in natural language.
- Users can ask questions about their dataset without writing formulas or code.

### Tagline

> Turn raw data into clear decisions.

### Core product principle

> **Pandas calculates. Gemma reasons and communicates.**

The AI must not invent numerical facts. Numerical claims shown to the user should originate from computed dataset evidence.

---

## 2. Problem

Raw datasets often contain useful information but require technical knowledge to understand.

A user receiving a CSV/XLSX file may need to:

- understand the schema,
- find missing or duplicate data,
- calculate statistics,
- identify trends,
- compare categories,
- discover anomalies,
- decide which findings matter,
- explain the results to someone else.

Traditional spreadsheet and BI tools help users visualize data, but they still require users to know what to investigate.

DataLens AI should reduce that analytical friction.

---

## 3. Target Users

### Primary

- Students
- Beginners learning data analysis
- Small business users
- Developers who need quick dataset exploration
- Non-technical users who receive structured data

### Secondary

- Hackathon participants
- Educators
- Analysts who need a quick first-pass analysis

---

## 4. Goals

### P0 — Must ship

1. Upload CSV and XLSX files.
2. Display dataset preview.
3. Profile dataset structure and quality.
4. Calculate basic numerical statistics.
5. Generate useful charts automatically.
6. Generate an AI-powered dataset summary using Gemma 4.
7. Provide an "Ask Your Data" interface.
8. Ground AI responses in computed evidence.
9. Run without a paid backend or database.
10. Provide a public open-source GitHub repository.

### P1 — Strong additions

1. Insight cards for trends, anomalies, and top performers.
2. Better chart recommendations.
3. Downloadable analysis/report output.
4. Demo-ready sample dataset.

### P2 — Optional wow feature

1. Upload a dashboard screenshot.
2. Ask Gemma 4 to interpret visible trends and metrics.
3. Present visual observations separately from numerical evidence.

---

## 5. Non-Goals

The hackathon MVP will NOT include:

- User accounts
- Authentication
- Multi-user collaboration
- Database persistence
- Paid APIs or required cloud AI services
- Payment systems
- Enterprise data warehouses
- SQL connectors
- Fine-tuning
- Complex autonomous agents
- Large-scale cloud infrastructure
- Dozens of file formats
- Full BI-platform replacement

---

## 6. User Journey

1. User opens DataLens AI.
2. User uploads CSV/XLSX.
3. DataLens loads the dataset.
4. Dataset overview appears.
5. Data quality checks run.
6. Basic statistics are calculated.
7. Relevant charts are generated.
8. User clicks "Generate AI Insights".
9. DataLens builds a compact evidence context.
10. Gemma 4 explains the findings.
11. User asks a natural-language question.
12. DataLens calculates relevant evidence.
13. Gemma 4 produces a grounded answer.
14. Optional: user uploads a dashboard screenshot for visual analysis.

---

## 7. Functional Requirements

### FR-01 File Upload

The system SHALL accept:

- `.csv`
- `.xlsx`
- `.xls` where practical

The MVP should prioritize CSV and XLSX.

### FR-02 Dataset Preview

The system SHALL display:

- number of rows,
- number of columns,
- first rows,
- column names,
- inferred data types.

### FR-03 Data Quality

The system SHALL calculate:

- missing values,
- missing percentage,
- duplicate rows,
- empty columns,
- unique-value counts,
- inferred types.

### FR-04 Statistics

For numerical columns, the system SHALL calculate where applicable:

- count,
- mean,
- median,
- minimum,
- maximum,
- standard deviation.

### FR-05 Automatic Visualization

The system SHOULD generate useful visualizations based on detected column types.

Examples:

- date + numerical measure → line chart,
- category + numerical measure → bar chart,
- numerical + numerical → scatter plot,
- categorical distribution → bar chart.

### FR-06 AI Summary

The system SHALL provide an AI summary using Gemma 4.

The prompt SHALL include verified analytical evidence.

### FR-07 Ask Your Data

The system SHALL allow a user to ask questions in natural language.

The application SHOULD determine which dataset calculations are relevant before asking Gemma for the explanation.

### FR-08 Evidence Grounding

AI responses SHALL be instructed to:

- use supplied evidence only,
- avoid inventing numbers,
- distinguish observations from recommendations,
- state uncertainty where evidence is insufficient.

### FR-09 Error Handling

The system SHALL handle:

- unsupported files,
- malformed CSV/XLSX files,
- empty datasets,
- missing API key,
- API errors,
- oversized inputs,
- unsupported questions.

### FR-10 API Key Security

The Gemini API key SHALL be read from an environment variable.

The key SHALL NOT be committed to GitHub.

---

## 8. Non-Functional Requirements

### Performance

For a normal demo dataset, upload and local profiling should feel near-instant.

### Reliability

The application should continue to provide local data analysis even if Ollama/Gemma is temporarily unavailable.

### Usability

A first-time user should understand the main workflow without documentation.

### Cost

The hackathon implementation SHALL avoid paid APIs and paid infrastructure.

### Reproducibility

The repository SHALL contain installation and run instructions.

### Open Source

The repository SHALL use an open-source license and disclose AI development/runtime usage as required by the event.

---

## 9. Success Criteria

The MVP is successful if a judge can:

1. Upload a dataset.
2. See meaningful quality metrics.
3. See useful charts.
4. Generate an AI summary.
5. Ask a data question.
6. Receive an answer tied to visible evidence.
7. Understand why Gemma 4 is useful in the application.

---

## 10. Demo Dataset

The repository should include a deterministic sample sales dataset containing:

- Date
- Product
- Category
- Region
- Quantity
- Revenue
- Cost
- Profit

The sample data should intentionally contain:

- a visible trend,
- a category leader,
- a regional difference,
- at least one anomaly,
- some missing values,
- a small number of duplicate rows.

This makes the demo predictable and testable.

---

## 11. Hackathon Constraints

The implementation must respect the event requirement that the project be built during the hacking period, use open-source/open-weight AI, be published in a public GitHub repository with an open-source license, and credit AI coding tools used in the README.

---

## 12. Future Vision

After the hackathon, DataLens AI could expand into:

- natural-language chart generation,
- SQL/database connectors,
- scheduled reports,
- collaborative analysis,
- richer anomaly detection,
- multilingual explanations,
- report export,
- dashboard screenshot analysis,
- local/offline model support.

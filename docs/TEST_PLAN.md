# DataLens AI — Test Plan

## 1. File Upload Tests

### CSV

- valid CSV loads
- empty CSV handled
- malformed CSV handled
- encoding issues handled where practical

### XLSX

- valid workbook loads
- empty worksheet handled
- invalid file handled

---

## 2. Data Profiling Tests

Verify:

- row count
- column count
- missing values
- duplicate rows
- data types
- unique values

Use a small known dataset with manually verified expected results.

---

## 3. Statistics Tests

Test:

- mean
- median
- min
- max
- count
- standard deviation
- grouped sums
- grouped averages

Results must match expected values.

---

## 4. Visualization Tests

Check:

- chart renders
- correct axis labels
- correct values
- no chart for unsupported data
- empty groups do not crash the app

---

## 5. AI Tests

### Grounding

Ask:

> What is total revenue?

Expected:

The response must match the calculated value.

### Unsupported question

Ask something unrelated to the dataset.

Expected:

The model should state that the available evidence is insufficient.

### Hallucination resistance

Ask for a nonexistent category.

Expected:

The model must not invent one.

### Trend question

Ask:

> Why did revenue fall in March?

Expected:

The answer should reference calculated evidence and avoid unsupported causal claims.

---

## 6. Security Tests

- API key not visible in source
- `.env` ignored
- no secrets committed
- no API key printed in UI

---

## 7. Demo Smoke Test

Before presentation:

1. Start application.
2. Load sample dataset.
3. Verify overview.
4. Verify quality report.
5. Verify charts.
6. Generate AI summary.
7. Ask three prepared questions.
8. Optionally test screenshot analysis.
9. Restart application.
10. Repeat once.

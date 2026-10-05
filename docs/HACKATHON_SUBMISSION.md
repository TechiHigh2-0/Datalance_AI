# DataLens AI — Hackathon Submission Brief

## Project Name

DataLens AI

## Tagline

Turn raw data into clear decisions.

## One-Sentence Pitch

DataLens AI is a free AI data analyst that uses Gemma 4 to turn CSV/Excel datasets into evidence-backed insights, visualizations, and natural-language answers.

## Problem

People often receive datasets but lack the time or technical knowledge to identify the most important findings.

## Solution

DataLens combines deterministic Python/Pandas analysis with Gemma 4 reasoning:

```text
Dataset
 ↓
Pandas analysis
 ↓
Verified evidence
 ↓
Gemma 4
 ↓
Human-readable insights
```

## Why Gemma 4?

Gemma 4 is used as the reasoning and explanation layer and can optionally analyze dashboard images.

The model is not used as a calculator. This deliberate separation improves trustworthiness.

## Key Features

1. Dataset profiling
2. Data-quality analysis
3. Automatic visualizations
4. AI-generated insights
5. Ask Your Data
6. Optional multimodal dashboard analysis

## What Makes It Different?

DataLens is designed around:

> **Evidence first, explanation second.**

Python computes the numbers. Gemma explains what those numbers mean.

## Demo Flow

1. Upload sales dataset.
2. Show dataset health.
3. Show automatic charts.
4. Generate AI insights.
5. Ask: "Why did revenue fall in March?"
6. Show evidence.
7. Show Gemma's explanation.
8. Optionally demonstrate dashboard screenshot analysis.

## Open Source

Public GitHub repository with open-source license.

## AI Disclosure

AI coding tools were used during development and will be credited in the repository README.

## Cost

The intended hackathon implementation uses free/open-source software and free-tier AI access. No paid API or paid infrastructure is required for the MVP.

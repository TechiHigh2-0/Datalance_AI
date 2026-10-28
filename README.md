# DataLens AI 🔍

> **Turn raw data into clear decisions.**
>
> Pandas calculates. AI reasons and communicates.

DataLens AI is an AI-assisted data exploration application that helps users understand CSV and Excel datasets without writing code. It combines Python-based data analysis with AI-powered explanations, allowing users to inspect data quality, explore statistics, generate interactive visualizations, and ask questions about their data in natural language.

## ✨ Features

- 📂 **CSV and Excel Upload** — Upload `.csv` and `.xlsx` datasets for analysis.
- 👀 **Dataset Preview** — Explore uploaded data in an interactive table.
- 🔍 **Dataset Profiling** — Examine row counts, column counts, missing values, duplicate rows, and data types.
- 📊 **Descriptive Statistics** — Review numerical and categorical summaries.
- 📈 **Automatic Visualizations** — Generate interactive charts using Plotly.
- 🤖 **AI-Assisted Analysis** — Use the configured AI integration to explain analytical findings.
- 💬 **Ask Your Data** — Ask questions about your dataset in natural language.
- 🧠 **Evidence-Based Insights** — Keep numerical calculations in Python and use AI to explain the results.
- 🧪 **Sample Dataset** — Try the application with the included sales dataset.
- 📚 **Developer Documentation** — Explore technical specifications, development plans, and testing documentation.

> **Note:** AI-generated responses can contain errors. Verify important findings against the original dataset and calculated statistics.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Pandas | Data loading, profiling, and analysis |
| Plotly | Interactive charts and visualizations |
| openpyxl | Excel workbook support |
| python-dotenv | Environment variable management |
| google-genai | Google Gen AI SDK dependency for AI integration |
| Git and GitHub | Version control and collaboration |

The repository includes documentation for the Gemma model strategy. Refer to `src/ai/` and the project documentation before changing model names, providers, or runtime configuration.

## 📁 Project Structure

```text
Datalance_AI/
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   └── sample_sales.csv
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── profiler.py
│   ├── statistics.py
│   ├── visualizations.py
│   ├── ask_data.py
│   ├── evidence.py
│   └── ai/
│       ├── __init__.py
│       ├── gemma_service.py
│       └── prompts.py
│
├── tests/
│   ├── __init__.py
│   ├── test_phase2.py
│   └── test_phase3.py
│
├── test_advanced.py
│
└── docs/
    ├── PRD.md
    ├── TECHNICAL_DESIGN.md
    ├── AI_SPEC.md
    ├── UX_SPEC.md
    ├── TEST_PLAN.md
    ├── DEVELOPMENT_PLAN.md
    ├── CONTRIBUTING.md
    ├── DOCUMENT_INDEX.md
    ├── HACKATHON_SUBMISSION.md
    ├── RISKS_AND_DECISIONS.md
    └── ANTIGRAVITY_PROMPTS.md
```

## 🚀 Getting Started

Follow these instructions to run DataLens AI locally.

### Prerequisites

Make sure you have installed:

- Python 3.10 or newer recommended
- Git
- pip
- An internet connection if your configured AI service requires one

### 1. Clone the Repository

```bash
git clone https://github.com/TechiHigh2-0/Datalance_AI.git
cd Datalance_AI
```

### 2. Create a Virtual Environment

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Upgrade pip and install the required packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a local environment file from the provided example.

**Windows — PowerShell**

```powershell
Copy-Item .env.example .env
```

**macOS / Linux**

```bash
cp .env.example .env
```

Open `.env` and configure the credentials required by the AI integration.

The current example file contains a placeholder:

```env
GOOGLE_API_KEY=your_api_key_here
```

Replace the placeholder with the appropriate credential if required by the configured provider.

**Security reminders:**

- Never commit your `.env` file.
- Never publish API keys in source code or screenshots.
- Never share credentials in public issues or pull requests.
- Check `src/ai/gemma_service.py` and `docs/AI_SPEC.md` for the actual AI runtime configuration.

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will display a local URL, typically:

```text
http://localhost:8501
```

Open this address in your browser to use DataLens AI.

## 📊 How to Use

### Step 1: Upload a Dataset

Launch the application and upload a CSV or Excel file through the sidebar.

You can also try the included sample dataset:

`data/sample_sales.csv`

### Step 2: Preview Your Data

Inspect the uploaded dataset in the preview table.

Review the available columns, records, and overall structure before proceeding.

### Step 3: Profile the Dataset

Review the profiling information provided by the application, including:

- Total number of rows
- Total number of columns
- Duplicate rows
- Missing values
- Column data types

Use these metrics to identify potential data quality issues.

### Step 4: Explore Statistics

Examine the numerical and categorical statistics generated by the application.

These summaries can help you understand distributions, ranges, and differences across columns.

### Step 5: Explore Visualizations

Review the automatically generated Plotly charts.

Interactive charts can help reveal patterns, comparisons, and potential trends in the dataset.

### Step 6: Ask Your Data

Enter a question in the **Ask Your Data** section and select **Ask Gemma** to request an AI-generated explanation.

#### Example Questions

- What are the top five products by revenue?
- Which region contributes the most revenue?
- How has revenue changed over time?
- Which category performs best?
- Are there unusual revenue values?
- Compare the performance of different regions.
- Analyze the relationship between quantity and revenue.
- Summarize the most important findings in this dataset.

The answers depend on the dataset's columns, the analytical evidence generated by the application, and the configured AI service.

## 🧠 How It Works

DataLens AI separates numerical computation from natural-language interpretation.

```text
             User Uploads Dataset
                      |
                      v
              Streamlit Interface
                      |
                      v
                  Data Loader
                      |
                      v
              Pandas Data Analysis
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      Profiling    Statistics   Charts
          |           |           |
          +-----------+-----------+
                      |
                      v
             Analytical Evidence
                      |
                      v
                AI Integration
                      |
                      v
           Natural-Language Insights
```

### Pandas — Numerical Analysis

Pandas handles deterministic data operations, including:

- Dataset profiling
- Missing-value analysis
- Duplicate detection
- Descriptive statistics
- Data grouping and aggregation
- Numerical calculations

### Plotly — Visualization

Plotly presents supported data through interactive charts that help users explore patterns and comparisons.

### AI — Interpretation and Explanation

The AI integration is designed to help users:

- Understand analytical findings
- Summarize patterns
- Ask questions about data
- Interpret calculated evidence
- Explore possible next steps

The AI should not invent numerical facts or claim that a trend proves causation without supporting evidence.

## 🧪 Running Tests

The repository contains automated tests under `tests/` and an additional test file named `test_advanced.py`.

Run the tests in the `tests` directory using Python's unittest discovery:

```bash
python -m unittest discover -s tests
```

Alternatively, if pytest is installed, run:

```bash
python -m pip install pytest
pytest
```

Test coverage may vary. Passing tests do not guarantee that every dataset, edge case, or AI-generated response will behave correctly.

## 🔐 Privacy and Security

DataLens AI is intended to make dataset exploration easier, but users should take care when working with sensitive information.

- Keep environment files and credentials private.
- Do not upload confidential, personal, or regulated data unless you understand how it is processed.
- Review the configured AI provider's data-handling policies before submitting sensitive datasets.
- Only analyze datasets you have permission to use.
- Verify AI-generated conclusions before relying on them for important decisions.
- Avoid exposing private dataset contents in public bug reports or screenshots.

## ⚠️ Limitations

- Supported file formats and behavior depend on the implemented data loader.
- Very large datasets may require additional memory and processing time.
- Automatic charts depend on the available columns and data types.
- AI answers depend on the evidence generated and the configured model.
- AI-generated explanations may omit context or misinterpret a result.
- The project is not a replacement for expert analysis or a full business intelligence platform.
- AI features may be unavailable if the configured provider, model, or required credentials are unavailable.

## 🛠️ Troubleshooting

### Application Does Not Start

1. Confirm Python is installed.
2. Activate your virtual environment.
3. Install dependencies again:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application from the repository root:

   ```bash
   streamlit run app.py
   ```

### Dataset Upload Fails

- Verify that the file is a valid CSV or XLSX file.
- Check for malformed rows or unsupported encodings.
- Try a smaller dataset.
- Confirm the Excel workbook is not damaged or empty.

### AI Questions Fail

- Check the environment variables required by the configured AI service.
- Review the configuration in `src/ai/gemma_service.py`.
- Confirm the selected model and provider are available.
- Check connectivity and API quota limits where applicable.
- Review the error message displayed by the application.

### Charts Are Not Generated

- Check whether the dataset contains usable numerical or categorical columns.
- Verify that the uploaded data loaded correctly.
- Inspect the application output for data-processing errors.

### Dependencies Fail to Install

- Confirm that your Python version is compatible with the packages.
- Upgrade pip.
- Recreate the virtual environment if it is corrupted.
- Check the installation output for package-specific errors.

## 📚 Documentation

More detailed technical and project documentation is available in the `docs/` directory.

| Document | Description |
|---|---|
| [Product Requirements](docs/PRD.md) | Product goals, scope, user journey, and requirements |
| [Technical Design](docs/TECHNICAL_DESIGN.md) | Architecture and technical implementation plan |
| [AI Specification](docs/AI_SPEC.md) | AI behavior, prompt strategy, and evidence grounding |
| [UX Specification](docs/UX_SPEC.md) | User experience requirements |
| [Development Plan](docs/DEVELOPMENT_PLAN.md) | Development milestones and implementation planning |
| [Test Plan](docs/TEST_PLAN.md) | Testing strategy |
| [Contribution Guidelines](docs/CONTRIBUTING.md) | Instructions for contributors |
| [Document Index](docs/DOCUMENT_INDEX.md) | Index of project documentation |
| [Hackathon Submission](docs/HACKATHON_SUBMISSION.md) | Project submission information |
| [Risks and Decisions](docs/RISKS_AND_DECISIONS.md) | Documented risks and design decisions |

## 🤝 Contributing

Contributions, bug reports, documentation improvements, and feature suggestions are welcome.

### Contribution Steps

1. Fork the repository.
2. Create a branch for your change.
3. Make your changes.
4. Add or update tests when applicable.
5. Run the relevant tests.
6. Open a pull request with a clear explanation of your changes and how you tested them.

For project-specific guidance, see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

### Contribution Guidelines

- Keep numerical calculations deterministic.
- Keep AI prompts explicit and grounded in evidence.
- Avoid placing numerical computation in the AI layer when Python can perform it reliably.
- Never commit API keys.
- Add tests for new analytical logic.
- Keep changes focused and maintainable.
- Document important configuration changes.

## 🗺️ Roadmap

Potential future improvements include:

- More advanced automatic chart recommendations
- Downloadable analysis reports
- Improved anomaly detection
- Natural-language chart generation
- More sophisticated analytical question handling
- Enhanced dataset summaries
- Additional file-format support
- Dashboard screenshot interpretation
- Improved error handling and AI fallback behavior
- More comprehensive automated testing

These are potential future enhancements, not a statement that every feature is currently implemented.

## 📄 License

The project's contribution documentation refers to the **Apache License 2.0**.

Before redistributing or modifying the project, verify that the repository contains the corresponding `LICENSE` file and review its terms.

## 👥 Project

**Repository:** [TechiHigh2-0/Datalance_AI](https://github.com/TechiHigh2-0/Datalance_AI)

DataLens AI is built to make data analysis easier to understand by combining Python-based calculations, interactive visualizations, and AI-assisted explanations.

---

<p align="center">
  <strong>DataLens AI 🔍</strong><br>
  Turn raw data into clear decisions.
</p>

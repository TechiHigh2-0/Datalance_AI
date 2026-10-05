# Contributing to DataLens AI

Thanks for your interest in contributing.

## Development Setup

```bash
python -m venv .venv
pip install -r requirements.txt
streamlit run app.py
```

## Guidelines

- Keep data calculations deterministic.
- Do not move numerical computation into the LLM layer without a strong reason.
- Keep AI prompts explicit and grounded.
- Never commit API keys.
- Add tests for new analytical logic.
- Keep the MVP simple and maintainable.

## Pull Requests

Please include:

- what changed,
- why it changed,
- how it was tested.

## License

By contributing, you agree that your contributions are provided under the project's Apache License 2.0.

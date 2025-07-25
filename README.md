# Team Training Repo

This repo simulates a **real-life dev team workflow**.

## Workflow
1. Create a branch using `feature/<your-change>`
2. Make edits (Python, YAML, or JSON)
3. Open a Pull Request
4. CI will:
   - Lint Python with Ruff
   - Validate YAML
   - Validate JSON
5. You cannot merge if checks fail!

## Tech stack
- Python 3.11
- Ruff for linting
- yamllint for YAML validation
- jsonlint for JSON validation
- pytest for basic tests

## How to run locally
```bash
pip install -r requirements.txt
pytest
ruff check .
yamllint .
find . -name '*.json' -exec jsonlint -q {} \;

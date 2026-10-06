# Study Assistant — starter

A starter repository for the CSC10014 Smart Virtual Assistant project.

## Setup

Prerequisites: Python 3.10+, Git.

```bash
git clone https://github.com/YinceIuCode/assistant-team03.git
cd assistant-team03
python -m venv .venv

# On macOS / Linux / Git Bash:
source .venv/bin/activate
# On Windows PowerShell:
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
pip install -e .
```

## Run
```bash
python -m assistant "where is the library?"
```

## Test

```bash
pytest -q
```

## Project structure

* `src/`: Backend application code.
* `tests/`: Automated tests.
* `docs/`: Project documentation, logbooks, and reports.
* `data/`: Small, non-sensitive sample data.
* `ui/`: User interface components.
* `scripts/`: Helper scripts (e.g., check_env.py).
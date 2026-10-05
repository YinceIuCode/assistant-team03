# Smart Virtual Assistant — Lab 01 & Team Setup

Welcome to the **Smart Virtual Assistant** project. This repository contains the source code, setup configuration, environment verification scripts, tests, and documentation for our course lab and team assignment.

---

## 1. Setup Instructions

Follow these steps to set up the development environment, run the application, execute tests, and complete both individual and team workflows.

### Step 1: Get the starter Repository

1. Open the starter repository link on LMS and click **Use this template** $\rightarrow$ **Create a new repository** (or Fork). Name your repository `lab01-<github-username>`.
2. Open your terminal and run:

   ```bash
   mkdir -p ~/projects/csc10014 && cd ~/projects/csc10014
   git clone git@github.com:<your-username>/lab01-<your-username>.git
   cd lab01-<your-username>
   ```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv

# Activate environment on Linux/MacOS:
source .venv/bin/activate

# Activate environment for sexiest Linux rice:
source .venv/bin/activate.fish

# Activate environment on Windows (PowerShell):
# .venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
(.venv) $ pip install -r requirements.txt
(.venv) $ pip install -e .
```

### Step 4: Run the Application & Tests

```bash
# Run the CLI assistant with a query
(.venv) $ python -m assistant "where is the IT helpdesk?"

# Run automated tests
(.venv) $ pytest -q
```

### Step 5: Configure `.gitignore` & Verify Environment

1. Ensure `.gitignore` ignores the `.venv/` directory. Check with `git status` to confirm `.venv/` is not listed as untracked.
2. Run the environment checker script until all items pass:

   ```bash
   (.venv) $ python scripts/check_env.py
   ```

   *Target: Every line must report `[ OK ]`.*

### Step 6: Make Meaningful Commits & Tag Version

1. Make at least three commits using Conventional Commit format (e.g., `feat: ...`, `fix: ...`, `docs: ...`).
2. Tag your first release and push to GitHub:

   ```bash
   git tag v0.1
   git push origin main --tags
   ```

### Step 7: Pair Verification

1. Swap repository links with a peer.
2. Have your partner clone and run the project following **only** this `README.md` (no verbal guidance permitted).
3. Partner fills in `lab01/worksheets/pair_verification.md` and submits it to you.
4. Address any documentation issues, commit changes, and save the completed form to `docs/lab1/pair_verification.md`.

### Step 8: Team Project Skeleton & Pull Requests

For team integration, members create individual feature branches and submit Pull Requests (PRs) covering their assigned responsibility areas. Once all PRs are merged into `main`, tag the release:

```bash
git tag v0.1-setup
git push origin main --tags
```

---

## 2. Homework / Project Overview

This homework focuses on building a **Smart Virtual Assistant** CLI application using Python. Key learning outcomes and project deliverables include:

* **Developer Environment Setup:** Managing isolated Python virtual environments (`.venv`), package dependencies (`requirements.txt`, `pyproject.toml`), and environment verification scripts (`scripts/check_env.py`).
* **Source Code Architecture:** Developing core package logic under `src/assistant/`, user interface specifications under `ui/`, and structured datasets under `data/` (e.g., `offices.csv`).
* **Testing & Quality Assurance:** Writing unit and integration tests using `pytest` inside the `tests/` directory to ensure reliable responses for location queries and assistant interactions.
* **Collaborative Git Workflow:** Practicing professional software engineering workflows including feature branching, conventional commit standards, Pull Request (PR) peer reviews, and semantic release tagging (`v0.1`, `v0.1-setup`).

---

## 3. Team Member Task Assignments

For detailed information regarding team members, Student IDs, roles, and assigned PR tasks, please refer to the dedicated team documentation:

👉 **[View Team Members & Task Assignments](docs/team.md)**
